from django.conf.urls import url, include 
from venta.views import indexVenta

urlpatterns = [
url(r'^$', indexVenta),
]
