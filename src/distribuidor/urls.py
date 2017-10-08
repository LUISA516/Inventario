from django.conf.urls import url, include
from distribuidor.views import index

urlpatterns = [
url(r'^$', index),
]