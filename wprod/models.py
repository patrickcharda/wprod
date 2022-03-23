from unittest.util import _MAX_LENGTH
from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class BL_Entete(models.Model):
    bl_num = models.BigIntegerField(primary_key=True) # CLE PRIMAIRE
    bl_cial = models.CharField(max_length=30, blank=True, null=True)
    bl_date = models.DateTimeField(blank=True, null=True)
    bl_dateimport = models.DateTimeField(blank=True, null=True)
    bl_nomclient = models.CharField(max_length=50, null=True, blank=True)
    bl_refclient = models.CharField(max_length=70, null=True, blank=True)
    bl_chantier = models.CharField(max_length=15, blank=True, null=True)
    bl_adr1liv = models.CharField(max_length=30, blank=True, null=True)
    bl_adr2liv = models.CharField(max_length=30, blank=True, null=True)
    bl_adr3liv = models.CharField(max_length=30, blank=True, null=True)
    bl_cpliv = models.CharField(max_length=5, blank=True, null=True)
    bl_villeliv = models.CharField(max_length=30, blank=True, null=True)
    bl_observ = models.TextField(max_length=2000, blank=True, null=True)
    bl_comment = models.TextField(max_length=2000, blank=True, null=True)
    
    class Meta:
        ordering = ('bl_num',)
    
    def __str__(self):
        return self.bl_num + " " + self.bl_nomclient + " " + self.bl_chantier + " " + self.bl_villeliv
    
class BL_Ligne(models.Model):
    UNITE_CHOICES = [
        ('ML', 'Mètre linéaire'), # 'valeur en bdd', 'valeur utilisateur' / ligne.bli_unite affiche valeur db, ligne.get_bli_unite_display() affiche val util
        ('UN', 'Unité'),
        ('M2', 'Mètre carré'),
        ('KG', 'Kilogramme'),
        ('M3', 'Mètre cube'),
        ('TO', 'Tonne'),
    ]
    bli_bl_num = models.ForeignKey( # CLE ETRANGERE
        BL_Entete,
        null=True,
        related_name="lignes",
        blank=True,
        on_delete=models.CASCADE)
    bli_num = models.BigIntegerField(primary_key=True) # CLE PRIMAIRE
    # bli_bl_num = models.BigIntegerField(null=True, blank=True)
    bli_select = models.BooleanField(default=False, blank=True, null=True)
    bli_codeproduit = models.BigIntegerField(blank=True, null=True)
    bli_libel = models.CharField(max_length=60, blank=True, null=True)
    bli_qte = models.FloatField(blank=True, null=True)
    bli_observ = models.TextField(max_length=2000, blank=True, null=True)
    bli_comment = models.TextField(max_length=2000, blank=True, null=True)
    bli_pu = MoneyField(max_digits=19, decimal_places=2, null=True, default_currency='EUR')
    bli_unite = models.CharField(
        max_length=3,
        blank=True,
        choices = UNITE_CHOICES,
        null=True
    )
    
    class Meta:
        ordering = ('bli_num', 'bli_codeproduit')
        
    def __str__(self):
        return "N°ligne: " + self.bli_num + "N°bl: " + self.bli_bl_num + "Pdt: " + self.bli_codeproduit
    
    
