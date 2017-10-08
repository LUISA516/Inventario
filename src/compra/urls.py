from django.conf.urls import url
from compra.views import indexCompra


urlpatterns = [
url(r'^$', indexCompra),
]