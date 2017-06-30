from channels import Group
from channels.auth import channel_session_user_from_http
from .models import Chatter
import json
from django.dispatch import receiver
from .views import real_time_send


@receiver(signal=real_time_send, sender='post')
def real_time(sender, to, toss, width, margin, **kwargs):
    Group(to).send({"text": json.dumps({"msg": toss, "wide": width, "margin_shift": margin})})


@channel_session_user_from_http
def incoming(message):
    if message.user.is_authenticated():
        message.reply_channel.send({"accept": True})
        msg_to = Chatter.objects.get(user=message.user)
        Group(msg_to.status_code).add(message.reply_channel)


@channel_session_user_from_http
def online(message):
    if message.user.is_authenticated():
        message.reply_channel.send({"accept": True})
        set_user_status = Chatter.objects.get(user=message.user)
        set_user_status.status_code = str(message.content['reply_channel']).split('!')[1]
        set_user_status.save()

    else:
        message.reply_channel.send({"accept": False})


def offline(message):
    set_user_status = Chatter.objects.get(status_code=str(message.content['reply_channel']).split('!')[1])
    set_user_status.status_code = '#'
    set_user_status.save()
