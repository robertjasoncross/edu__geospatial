# Generated by Django 2.2.5 on 2019-09-11 04:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arenas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=30)),
                ('subsector', models.CharField(max_length=22)),
                ('primary_ty', models.CharField(max_length=45)),
                ('date_creat', models.CharField(max_length=15)),
                ('date_modif', models.CharField(max_length=24)),
                ('comp_affil', models.CharField(max_length=29)),
                ('name1', models.CharField(max_length=66)),
                ('name2', models.CharField(max_length=26)),
                ('name3', models.CharField(max_length=10)),
                ('address1', models.CharField(max_length=29)),
                ('address2', models.CharField(max_length=20)),
                ('po_box', models.CharField(max_length=24)),
                ('po_zip', models.CharField(max_length=24)),
                ('city', models.CharField(max_length=14)),
                ('state', models.CharField(max_length=4)),
                ('zip', models.CharField(max_length=6)),
                ('zip_4', models.CharField(max_length=12)),
                ('county', models.CharField(max_length=19)),
                ('hsip_aoi', models.CharField(max_length=23)),
                ('fema_regio', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('reliabilit', models.CharField(max_length=16)),
                ('coorsource', models.CharField(max_length=14)),
                ('comments_1', models.CharField(max_length=93)),
                ('conference', models.CharField(max_length=16)),
                ('division', models.CharField(max_length=16)),
                ('capacity', models.FloatField()),
                ('team', models.CharField(max_length=30)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]