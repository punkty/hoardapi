from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets

from resources.models import (
    Armor,
    MagicalProperty,
    Mount,
    Potion,
    Tool,
    Trinket,
    Weapon,
)
from resources.serializers import (
    ArmorSerializer,
    MagicalPropertySerializer,
    MountSerializer,
    PotionSerializer,
    ToolSerializer,
    TrinketSerializer,
    WeaponSerializer,
)
class ArmorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer

class MagicalPropertyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MagicalProperty.objects.all()
    serializer_class = MagicalPropertySerializer

class MountViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mount.objects.all()
    serializer_class = MountSerializer

class PotionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Potion.objects.all()
    serializer_class = PotionSerializer

class ToolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class TrinketViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Trinket.objects.all()
    serializer_class = TrinketSerializer

class WeaponViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

