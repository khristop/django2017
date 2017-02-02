from django.conf.urls import url
from views import inicio, principal

urlpatterns = [
    url(r'^$', inicio),
    url(r'inicio/$', principal),
]