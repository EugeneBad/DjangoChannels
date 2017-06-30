from django.db import models
from django.conf import settings


class Chatter(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    status_code = models.CharField(max_length=200, default='Offline')

    def __str__(self):
        return self.user.get_username()


class Toss(models.Model):
    receiver = models.ForeignKey(Chatter, related_name='received', null=True)
    sender = models.ForeignKey(Chatter, related_name='sent', null=True)
    toss = models.CharField(max_length=250)
    wide = models.IntegerField(null=True)

    def margin_shift(self):
        msg_shift = 100 - int(self.wide)
        return str(msg_shift) + '%'

    def __str__(self):

        return 'From: {f}, To: {t}'.format(f=self.sender, t=self.receiver)
