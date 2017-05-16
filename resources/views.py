from django.shortcuts import render
from rest_framework import generics
from resources.models import (
    Armor,
    Potion,
    Trinket,
)
from resources.serializers import (
    ArmorSerializer,
    PotionSerializer,
    TrinketSerializer,
)

class ArmorList(generics.ListCreateAPIView):
    """
    List all the armors.
    """
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer


class ArmorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an armor.
    """
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer


class PotionList(generics.ListAPIView):
    """
    List all potions 
    """
    queryset = Potion.objects.all()
    serializer_class = PotionSerializer

class PotionDetail(generics.ListAPIView):
    """
    Retrieve, update or delete a potion.
    """
    queryset = Potion.objects.all()
    serializer_class = PotionSerializer

