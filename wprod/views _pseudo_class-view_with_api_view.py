from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from wprod.models import BL_Entete, BL_Ligne
from wprod.serializers import BL_EnteteSerializer, BL_LigneSerializer
from django.views.decorators.csrf import csrf_exempt


        
@csrf_exempt
@api_view(['GET', 'POST'])
def bl_list(request):
    if request.method == 'GET':
        bls = BL_Entete.objects.all()
        bls_serialized = BL_EnteteSerializer(bls, many=True)
        return Response(bls_serialized.data)
    
    elif request.method == 'POST':
        bl_serialized = BL_EnteteSerializer(data=request.data)
        if bl_serialized.is_valid():
            bl_serialized.save()
            return Response(bl_serialized.data, status = status.HTTP_201_CREATED)
        return Response(bl_serialized.errors, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def bl_detail(request, pk):
    try:
        bl = BL_Entete.objects.get(pk=pk)
    except BL_Entete.DoesNotExist :
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        bl_serialized = BL_EnteteSerializer(bl)
        return Response(bl_serialized.data)
    
    elif request.method == 'PUT':
        bl_serialized = BL_EnteteSerializer(bl, data=request.data)
        if bl_serialized.is_valid():
            bl_serialized.save()
            return Response(bl_serialized.data, status = status.HTTP_201_CREATED)
        return Response(bl_serialized.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'POST'])
def bli_list(request):
    if request.method == 'GET':
        blis = BL_Ligne.objects.all()
        blis_serialized = BL_LigneSerializer(blis, many=True)
        return Response(blis_serialized.data)
    
    elif request.method == 'POST':
        # bli_data = JSONParser().parse(request)
        bli_serialized = BL_LigneSerializer(data=request.data)
        if bli_serialized.is_valid():
            bli_serialized.save()
            return Response(bli_serialized.data, status = status.HTTP_201_CREATED)
        return Response(bli_serialized.errors, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def bli_detail(request, pk):
    try:
        bli = BL_Ligne.objects.get(pk=pk)
    except BL_Ligne.DoesNotExist :
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        bli_serialized = BL_LigneSerializer(bli)
        return Response(bli_serialized.data)
    
    elif request.method == 'PUT':
        bli_serialized = BL_LigneSerializer(bli, data=request.data)
        if bli_serialized.is_valid():
            bli_serialized.save()
            return Response(bli_serialized.data, status = status.HTTP_201_CREATED)
        return Response(bli_serialized.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bli.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


