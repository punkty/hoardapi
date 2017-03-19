from django.conf.urls import url
from resources import views

urlpatterns = [
    url(r'^armors/$', views.armorList),
    url(r'^armors/(?P<pk>[0-9]+)/$', views.armorDetail),
]