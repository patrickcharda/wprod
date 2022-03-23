from rest_framework import serializers
from wprod.models import BL_Entete, BL_Ligne


class BL_EnteteSerializer(serializers.ModelSerializer):
    class Meta:  
        model = BL_Entete
        fields = (
            'bl_num',
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

class BL_LigneSerializer(serializers.ModelSerializer):
    class Meta:  
        model = BL_Ligne
        fields = (
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

