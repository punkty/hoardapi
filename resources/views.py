from django.shortcuts import render
from rest_framework import generics
from resources.models import (
    Armor,
    Mount,
    Potion,
    Tool,
    Trinket,
    Weapon,
)
from resources.serializers import (
    ArmorSerializer,
    MountSerializer,
    PotionSerializer,
    ToolSerializer,
    TrinketSerializer,
    WeaponSerializer,
)

class ArmorList(generics.ListCreateAPIView):
    """
    List all the armors.
    """
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer


class ArmorDetail(generics.RetrieveAPIView):
    """
    Retrieve, update or delete an armor.
    """
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer

class MountList(generics.ListAPIView):
    """
    List all mounts
    """
    queryset = Mount.objects.all()
    serializer_class = MountSerializer

class MountDetail(generics.RetrieveAPIView):
    """
    Retrieve single Mount
    """
    queryset = Mount.objects.all()
    serializer_class = MountSerializer

class PotionList(generics.ListAPIView):
    """
    List all potions
    """
    queryset = Potion.objects.all()
    serializer_class = PotionSerializer

class PotionDetail(generics.RetrieveAPIView):
    """
    Retrieve a potion.
    """
    queryset = Potion.objects.all()
    serializer_class = PotionSerializer

class ToolList(generics.ListAPIView):
    """
    List all Tools
    """
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class ToolDetail(generics.RetrieveAPIView):
    """
    Retrieve, a tool.
    """
    queryset = Trinket.objects.all()
    serializer_class = TrinketSerializer

class TrinketList(generics.ListAPIView):
    """
    List all trinkets
    """
    queryset = Trinket.objects.all()
    serializer_class = TrinketSerializer

class TrinketDetail(generics.RetrieveAPIView):
    """
    Retrieve, update or delete a potion.
    """
    queryset = Trinket.objects.all()
    serializer_class = TrinketSerializer

class WeaponList(generics.ListAPIView):
    """
    List all weapons
    """
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class WeaponDetail(generics.RetrieveAPIView):
    """
    List all weapons
    """
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer