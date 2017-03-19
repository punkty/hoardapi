from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from resources.models import Armor
from resources.serializers import ArmorSerializer


@csrf_exempt
def armorList(request):
    """
    List all the armors or create a new armor.
    """
    if request.method == "GET":
        armors = Armor.objects.all()
        serializer = ArmorSerializer(armors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArmorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def armorDetail(request, pk):
    """
    Retrieve, update or delete armor.
    """
    try:
        armor = Armor.objects.get(pk=pk)
    except Armor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ArmorSerializer(armor)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArmorSerializer(armor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        armor.delete()
        return HttpResponse(status=204)
