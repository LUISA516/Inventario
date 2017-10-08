from django.conf.urls import url
from registro.views import index

urlpatterns = [
url(r'^$', index),
] 