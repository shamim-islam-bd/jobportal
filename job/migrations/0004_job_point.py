# Generated by Django 4.2.1 on 2023-05-22 05:40

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326),
        ),
    ]
