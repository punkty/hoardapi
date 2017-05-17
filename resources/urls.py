from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from resources import views

urlpatterns = [
    url(r'^armor/$', views.ArmorList.as_view()),
    url(r'^armor/(?P<pk>[0-9]+)/$', views.ArmorDetail.as_view()),
    url(r'^potion/$', views.PotionList.as_view()),
    url(r'^potion/(?P<pk>[0-9]+)/$', views.PotionDetail.as_view()),
    url(r'^mount/$', views.MountList.as_view()),
    url(r'^mount/(?P<pk>[0-9]+)/$', views.MountDetail.as_view()),
    url(r'^tool/$', views.ToolList.as_view()),
    url(r'^tool/(?P<pk>[0-9]+)/$', views.ToolDetail.as_view()),
    url(r'^trinket/$', views.TrinketList.as_view()),
    url(r'^trinket/(?P<pk>[0-9]+)/$', views.TrinketDetail.as_view()),
    url(r'^weapon/$', views.WeaponList.as_view()),
    url(r'^weapon/(?P<pk>[0-9]+)/$', views.WeaponDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)