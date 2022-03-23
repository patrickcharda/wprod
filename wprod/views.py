from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.decorators import api_view
from wprod.models import BL_Entete, BL_Ligne
from wprod.serializers import BL_EnteteSerializer, BL_LigneSerializer
from django.views.decorators.csrf import csrf_exempt


class BL_EnteteList(generics.ListCreateAPIView):
    queryset = BL_Entete.objects.all()
    serializer_class = BL_EnteteSerializer
    name='bl_entete-list'

class BL_EnteteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BL_Entete.objects.all()
    serializer_class = BL_EnteteSerializer
    name='bl_entete-detail'

class BL_LigneList(generics.ListCreateAPIView):
    queryset = BL_Ligne.objects.all()
    serializer_class = BL_LigneSerializer
    name='bl_ligne-list'

class BL_LigneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BL_Ligne.objects.all()
    serializer_class = BL_LigneSerializer
    name='bl_ligne-detail'
 
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'entetes': reverse(BL_EnteteList.name,request=request),
            'lignes': reverse(BL_LigneList.name, request=request),
        })