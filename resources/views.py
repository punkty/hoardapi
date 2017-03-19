from resources.models import Armor
from resources.serializers import ArmorSerializer
from rest_framework import generics



class ArmorList(generics.ListCreateAPIView):
    """
    List all the armors or create a new armor.
    """
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer


class ArmorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an armor.
    """
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer



