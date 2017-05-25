from __future__ import unicode_literals

from django.http import HttpResponse

import json


class JSONResponse():

    def __init__(self, resource):
        with open('resources/schemas/{0}.json'.format(resource)) as f:
            data = json.loads(f.read())
        self.data = data

    @property
    def response(self):
        return HttpResponse(
            json.dumps(self.data),
            content_type="application/json"
        )

def armor(request):
    return JSONResponse('armor').response

def armor_stats(request):
    return JSONResponse('armorstats').response

def magical_property(request):
    return JSONResponse('magicalproperty').response

def mount(request):
    return JSONResponse('mount').response

def potion(request):
    return JSONResponse('potion').response

def tool(request):
    return JSONResponse('tool').response

def trinket(request):
    return JSONResponse('trinket').response

def weapon(request):
    return JSONResponse('weapon').response

def weapon_stats(request):
    return JSONResponse('weaponstats').response