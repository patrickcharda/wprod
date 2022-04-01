from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from wprod.models import BL_Entete, BL_Ligne
from wprod.serializers import BL_EnteteSerializer, BL_LigneSerializer
from rest_framework import permissions
from rest_framework.throttling import ScopedRateThrottle



class BL_EnteteList(generics.ListCreateAPIView):
    throttle_scope = 'bl_entete-list'
    throttle_classes = (ScopedRateThrottle,)
    queryset = BL_Entete.objects.all()
    serializer_class = BL_EnteteSerializer
    name='bl_entete-list'
    filter_fields = (
        'bl_num','bl_nomclient','bl_cial','bl_chantier','bl_villeliv', 
    )
    search_fields = (
        'bl_num','bl_nomclient','bl_cial','bl_chantier','bl_villeliv','bl_refclient', 
    )
    ordering_fields = (
        'bl_num','bl_nomclient','bl_chantier','bl_villeliv',
    )
    permission_classes = (
    permissions.IsAuthenticated,
    )

class BL_EnteteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BL_Entete.objects.all()
    serializer_class = BL_EnteteSerializer
    name='bl_entete-detail'
    permission_classes = (
    permissions.IsAuthenticated,
    )

class BL_LigneList(generics.ListCreateAPIView):
    queryset = BL_Ligne.objects.all()
    serializer_class = BL_LigneSerializer
    name='bl_ligne-list'
    filter_fields = (
        'bli_bl_num','bli_num','bli_unite','bli_codeproduit','bli_select',
    )
    search_fields = (
        'bli_bl_num','bli_num','bli_codeproduit','bli_libel','bli_select',
    )
    ordering_fields = (
        'bli_bl_num','bli_num','bli_codeproduit',
    )
    permission_classes = (
    permissions.IsAuthenticated,
    )
    

class BL_LigneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BL_Ligne.objects.all()
    serializer_class = BL_LigneSerializer
    name='bl_ligne-detail'
    permission_classes = (
    permissions.IsAuthenticated,
    )
 
class ApiRoot(generics.GenericAPIView):
    throttle_scope = 'api-root'
    throttle_classes = (ScopedRateThrottle,)
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'entetes': reverse(BL_EnteteList.name,request=request),
            'lignes': reverse(BL_LigneList.name, request=request),
        })
    