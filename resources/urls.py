from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from resources import views

urlpatterns = [
    url(r'^armor/$', views.ArmorList.as_view()),
    url(r'^armor/(?P<pk>[0-9]+)/$', views.Armor.as_view()),
    url(r'^potion/$', views.PotionList.as_view()),
    url(r'^potion/(?P<pk>[0-9]+)/$', views.Potion.as_view()),
    url(r'^magicalproperty$', views.MagicalPropertyList.as_view()),
    url(r'^magicalproperty/(?P<pk>[0-9]+)/$', views.MagicalProperty.as_view()),
    url(r'^mount/$', views.MountList.as_view()),
    url(r'^mount/(?P<pk>[0-9]+)/$', views.Mount.as_view()),
    url(r'^tool/$', views.ToolList.as_view()),
    url(r'^tool/(?P<pk>[0-9]+)/$', views.Tool.as_view()),
    url(r'^trinket/$', views.TrinketList.as_view()),
    url(r'^trinket/(?P<pk>[0-9]+)/$', views.Trinket.as_view()),
    url(r'^weapon/$', views.WeaponList.as_view()),
    url(r'^weapon/(?P<pk>[0-9]+)/$', views.Weapon.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)