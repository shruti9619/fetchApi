# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_app.elpis2 import fetch_notifics
from django.core.cache import cache
import json
import sys
# Create your views here.



@api_view(["GET"])
def notification_api(request):
    notif = []
    if request.method == "GET":
        try:
            num = request.GET.get('limit')
            #s =0/0

            if num:
                limit = int(num)
            else:
                limit = 10

            notif = fetch_notifics(limit)

        except:
            print "exception occured"
            notif = ["Maybe an internal error occured. Please come back later."]
            return HttpResponse(json.dumps(notif), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #sys.setrecursionlimit(10000)
    cache.set('notif_cache', notif, '120')
    #cache
    #print cache.get('notif')
    return HttpResponse(json.dumps(notif, sort_keys=True, indent=4, ensure_ascii=True , separators=(',', ': ')),  status= status.HTTP_200_OK)
