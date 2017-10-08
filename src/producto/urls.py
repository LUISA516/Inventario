from django.conf.urls import url 
from producto.views import indexProducto

urlpatterns = [
url(r'^$', indexProducto),
]