"""inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from registro import views

urlpatterns = [
	#url(r'^', views.index, name='pagina principal'),
	url(r'^$', views.index, name='pagina principal'),

    url(r'^admin/', admin.site.urls),
    url(r'^distribuidor/', include ('distribuidor.urls', namespace='distribuidor')),
    url(r'^compra/', include ('compra.urls', namespace='compra')),
    url(r'^producto/', include ('producto.urls', namespace='producto')),
    url(r'^registro/', include ('registro.urls', namespace='registro')),
    url(r'^venta/', include ('venta.urls', namespace='venta')),

]
