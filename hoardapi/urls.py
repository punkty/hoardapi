"""hoardapi URL Configuration

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
from __future__ import unicode_literals
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from . import views as site_views
from resources import views as api_views
from resources import schemas
print(schemas)

router = routers.DefaultRouter()
router.register(r'armor', api_views.ArmorViewSet)
router.register(r'magicalproperty', api_views.MagicalPropertyViewSet)
router.register(r'mount', api_views.MountViewSet)
router.register(r'potion', api_views.PotionViewSet)
router.register(r'tool', api_views.ToolViewSet)
router.register(r'trinket', api_views.TrinketViewSet)
router.register(r'weapon', api_views.WeaponViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', site_views.index),
    url(r'^about$', site_views.about),
    url(r'^documentation$', site_views.documentation),
    url(r'^api/armor/schema$', schemas.armor),
    url(r'^api/armorstats/schema$', schemas.armor_stats),
    url(r'^api/magicalproperty/schema$', schemas.magical_property),
    url(r'^api/mount/schema$', schemas.mount),
    url(r'^api/potion/schema$', schemas.potion),
    url(r'^api/tool/schema$', schemas.tool),
    url(r'^api/trinket/schema$', schemas.trinket),
    url(r'^api/weapon/schema$', schemas.weapon),
    url(r'^api/weaponstats/schema$', schemas.weapon_stats),
    url(r'^api/', include(router.urls)),
]
urlpatterns += router.urls