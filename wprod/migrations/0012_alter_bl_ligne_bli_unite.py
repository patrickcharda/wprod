# Generated by Django 4.0.2 on 2022-03-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wprod', '0011_bl_ligne_bli_comment_bl_ligne_bli_observ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bl_ligne',
            name='bli_unite',
            field=models.CharField(blank=True, choices=[('ML', 'Mètre linéaire'), ('UN', 'Unité'), ('M2', 'Mètre carré'), ('KG', 'Kilogramme'), ('M3', 'Mètre cube'), ('TO', 'Tonne')], max_length=3),
        ),
    ]
