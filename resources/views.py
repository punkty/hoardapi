from django.shortcuts import render
from rest_framework import generics
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

class ArmorList(generics.ListAPIView):
    """
    List all the armors.
    """
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer


class Armor(generics.RetrieveAPIView):
    """
    Retrieve an Armor.
    """
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer

class MagicalPropertyList(generics.ListAPIView):
    """
    List all Magical properties
    """
    queryset = MagicalProperty.objects.all()
    serializer_class = MagicalPropertySerializer

class MagicalProperty(generics.RetrieveAPIView):
    """
    Retrieve a Magical property
    """
    queryset = MagicalProperty.objects.all()
    serializer_class = MagicalPropertySerializer


class MountList(generics.ListAPIView):
    """
    List all Mounts
    """
    queryset = Mount.objects.all()
    serializer_class = MountSerializer

class Mount(generics.RetrieveAPIView):
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

class Potion(generics.RetrieveAPIView):
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

class Tool(generics.RetrieveAPIView):
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

class Trinket(generics.RetrieveAPIView):
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

class Weapon(generics.RetrieveAPIView):
    """
    List all weapons
    """
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer