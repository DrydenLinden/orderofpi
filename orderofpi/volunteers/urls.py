from django.conf.urls import url

from . import views as volunteer_views

urlpatterns = [
    url(r'^assign/$', volunteer_views.assign, name='assign'),
    url(r'^signup/$', volunteer_views.sign_up, name='sign_up'),
    url(r'^schedule/$', volunteer_views.view_schedule, name='view_schedule'),
]