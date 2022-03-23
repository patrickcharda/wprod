from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from wprod.models import BL_Entete, BL_Ligne
from wprod.serializers import BL_EnteteSerializer, BL_LigneSerializer
from django.views.decorators.csrf import csrf_exempt

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
@csrf_exempt
def bl_list(request):
    if request.method == 'GET':
        bls = BL_Entete.objects.all()
        bls_serialized = BL_EnteteSerializer(bls, many=True)
        return JSONResponse(bls_serialized.data)
    
    elif request.method == 'POST':
        bl_data = JSONParser().parse(request)
        bl_serialized = BL_EnteteSerializer(data=bl_data)
        if bl_serialized.is_valid():
            bl_serialized.save()
            return JSONResponse(bl_serialized.data, status = status.HTTP_201_CREATED)
        return JSONResponse(bl_serialized.errors, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def bl_detail(request, pk):
    try:
        bl = BL_Entete.objects.get(pk=pk)
    except BL_Entete.DoesNotExist :
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        bl_serialized = BL_EnteteSerializer(bl)
        return JSONResponse(bl_serialized.data)
    
    elif request.method == 'PUT':
        bl_data = JSONParser().parse(request)
        bl_serialized = BL_EnteteSerializer(bl, data=bl_data)
        if bl_serialized.is_valid():
            bl_serialized.save()
            return JSONResponse(bl_serialized.data, status = status.HTTP_201_CREATED)
        return JSONResponse(bl_serialized.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bl.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def bli_list(request):
    if request.method == 'GET':
        blis = BL_Ligne.objects.all()
        blis_serialized = BL_LigneSerializer(blis, many=True)
        return JSONResponse(blis_serialized.data)
    
    elif request.method == 'POST':
        bli_data = JSONParser().parse(request)
        bli_serialized = BL_LigneSerializer(data=bli_data)
        if bli_serialized.is_valid():
            bli_serialized.save()
            return JSONResponse(bli_serialized.data, status = status.HTTP_201_CREATED)
        return JSONResponse(bli_serialized.errors, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def bli_detail(request, pk):
    try:
        bli = BL_Ligne.objects.get(pk=pk)
    except BL_Ligne.DoesNotExist :
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        bli_serialized = BL_LigneSerializer(bli)
        return JSONResponse(bli_serialized.data)
    
    elif request.method == 'PUT':
        bli_data = JSONParser().parse(request)
        bli_serialized = BL_LigneSerializer(bli, data=bli_data)
        if bli_serialized.is_valid():
            bli_serialized.save()
            return JSONResponse(bli_serialized.data, status = status.HTTP_201_CREATED)
        return JSONResponse(bli_serialized.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bli.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


