# Generated by Django 3.2.8 on 2021-10-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formdiagnosis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allergysymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coldsymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='musclesymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flatulencesymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='diarrheasymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='constipationsymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='allergiccontactsymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='urticariasymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='allergicweathersymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coldallergysymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accidentsymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parasitesymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coughsymptom',
            name='Sequence',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
