from django.shortcuts import render
from django.contrib.auth.views import login as login_view
from django.contrib.auth.views import logout as logout_view
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .forms import SentForm
from .models import Chatter, Toss
from django.contrib.auth.models import User
from django.dispatch import Signal


def login(request):
    return login_view(request, template_name='messenger/login.html')


def logout(request):
    return logout_view(request, template_name='messenger/login.html')


real_time_send = Signal(providing_args=["to", "toss", "width", "margin"])


class Chat(LoginRequiredMixin, View):
    def get(self, request):
        toss = Toss.objects.all()
        return render(request, template_name='messenger/toss.html', context={'toss': toss})

    def post(self, request):
        received_msg = SentForm(request.POST)

        recipient = Chatter.objects.get(user=User.objects.get(username=request.POST.get('receiver')))
        if received_msg.is_valid():
            msg_content = received_msg.pure_toss()
            msg_width = request.POST.get('wide')
            new_toss = Toss.objects.create(toss=msg_content, sender=Chatter.objects.get(user=request.user),
                                           receiver=recipient, wide=msg_width)
            new_toss.save()
            if recipient.status_code != '#':
                real_time_send.send(sender='post', to=recipient.status_code, toss=msg_content, width=msg_width,
                                    margin=new_toss.margin_shift())

        return HttpResponse()
