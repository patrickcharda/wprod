# Generated by Django 4.0.2 on 2022-03-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wprod', '0006_rename_bl_entete_bl_ligne_bl_entete_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_Adr1Liv',
            new_name='bl_adr1liv',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_Adr2Liv',
            new_name='bl_adr2liv',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_Adr3Liv',
            new_name='bl_adr3liv',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_Chantier',
            new_name='bl_chantier',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_Cial',
            new_name='bl_cial',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_Comment',
            new_name='bl_comment',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_CpLiv',
            new_name='bl_cpliv',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_Date',
            new_name='bl_date',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_NomClient',
            new_name='bl_nomclient',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_Num',
            new_name='bl_num',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_Observ',
            new_name='bl_observ',
        ),
        migrations.RenameField(
            model_name='bl_entete',
            old_name='BL_VilleLiv',
            new_name='bl_villeliv',
        ),
        migrations.RenameField(
            model_name='bl_ligne',
            old_name='BL_entete_id',
            new_name='bl_entete_id',
        ),
        migrations.RenameField(
            model_name='bl_ligne',
            old_name='BLI_BL_Num',
            new_name='bli_bl_Num',
        ),
        migrations.RenameField(
            model_name='bl_ligne',
            old_name='BLI_CodeProduit',
            new_name='bli_codeproduit',
        ),
        migrations.RenameField(
            model_name='bl_ligne',
            old_name='BLI_Libel',
            new_name='bli_libel',
        ),
        migrations.RenameField(
            model_name='bl_ligne',
            old_name='BLI_Num',
            new_name='bli_num',
        ),
        migrations.RenameField(
            model_name='bl_ligne',
            old_name='BLI_Qte',
            new_name='bli_qte',
        ),
        migrations.RenameField(
            model_name='bl_ligne',
            old_name='BLI_Select',
            new_name='bli_select',
        ),
        migrations.RenameField(
            model_name='bl_ligne',
            old_name='BLI_Unite',
            new_name='bli_unite',
        ),
        migrations.RemoveField(
            model_name='bl_entete',
            name='BL_RefClient',
        ),
        migrations.AddField(
            model_name='bl_entete',
            name='bl_refclient',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
