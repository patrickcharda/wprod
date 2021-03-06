# Generated by Django 4.0.2 on 2022-03-23 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wprod', '0018_rename_bl_entete_bl_ligne_bli_bl_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bl_entete',
            options={'ordering': ('bl_num',)},
        ),
        migrations.AlterModelOptions(
            name='bl_ligne',
            options={'ordering': ('bli_num', 'bli_codeproduit')},
        ),
        migrations.AlterField(
            model_name='bl_entete',
            name='bl_cial',
            field=models.CharField(blank=True, default='M.Test', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='bl_ligne',
            name='bli_bl_num',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lignes', to='wprod.bl_entete'),
        ),
    ]
