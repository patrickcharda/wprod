# Generated by Django 4.0.2 on 2022-03-10 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wprod', '0007_rename_bl_adr1liv_bl_entete_bl_adr1liv_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bl_ligne',
            old_name='bli_bl_Num',
            new_name='bli_bl_num',
        ),
    ]
