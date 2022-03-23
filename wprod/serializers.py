from rest_framework import serializers
from wprod.models import BL_Entete, BL_Ligne
#from wprod.views import *


class BL_EnteteSerializer(serializers.HyperlinkedModelSerializer):
    lignes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='bl_ligne-detail'
    )
    class Meta:  
        model = BL_Entete
        fields = (
            'url',
            'bl_num',
            'lignes',
            'bl_cial',
            'bl_date',
            'bl_dateimport',
            'bl_nomclient',
            'bl_refclient',
            'bl_chantier',
            'bl_adr1liv',
            'bl_adr2liv',
            'bl_adr3liv',
            'bl_cpliv',
            'bl_villeliv',
            'bl_observ',
            'bl_comment'
        )

class BL_LigneSerializer(serializers.HyperlinkedModelSerializer):
    bli_bl_num = serializers.SlugRelatedField(queryset=BL_Entete.objects.all(),
    slug_field='bl_num')
    class Meta:  
        model = BL_Ligne
        fields = (
            'url',
            'bli_bl_num',
            'bli_num',
            'bli_select',
            'bli_codeproduit',
            'bli_libel',
            'bli_qte',
            'bli_observ',
            'bli_comment',
            'bli_pu',
            'bli_unite'
        )

