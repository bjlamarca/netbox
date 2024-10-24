# Generated by Django 5.0.9 on 2024-10-23 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
        ('tenancy', '0015_contactassignment_rename_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiledevice',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mobile_device_tenant_set', to='tenancy.tenant'),
        ),
    ]
