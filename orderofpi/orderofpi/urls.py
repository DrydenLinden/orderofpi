"""orderofpi URL Configuration"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from . import views as orderofpi_views

urlpatterns = [
    url(r'^$', orderofpi_views.home, name='home'),
    url(r'^about/$', orderofpi_views.about, name='about'),
    url(r'^rules/$', orderofpi_views.about, name='rules'),
    url(r'^ranks/$', orderofpi_views.about, name='ranks'),
    url(r'^volunteer/', include('volunteers.urls')),
    url(r'^contract/', include('contracts.urls')),
    url(r'^payments/', include('payments.urls', namespace='payments')),
    url(r'^admin/', admin.site.urls),
]
