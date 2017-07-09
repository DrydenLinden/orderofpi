"""contracts URL Configuration"""

from django.conf.urls import url

from . import views as contract_views

urlpatterns = [
    url(r'^create/$', contract_views.create_contract, name='create_contract'),
    url(r'^extend/$', contract_views.extend_contract, name='extend_contract'),
]