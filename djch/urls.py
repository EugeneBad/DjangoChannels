from django.conf.urls import url
from django.contrib import admin
from Messenger.views import login, logout, Chat


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, name='login_url'),
    url(r'^$', Chat.as_view(), name='chat_url'),
    url(r'^logout/$', logout, name='logout_url'),
]

from django.contrib.auth.models import User