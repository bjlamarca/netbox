# Generated by Django 5.0.9 on 2024-10-15 17:58

import django.core.validators
import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('circuits', '0044_circuit_groups'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('dcim', '0190_nested_modules'),
        ('extras', '0121_customfield_related_object_filter'),
        ('tenancy', '0015_contactassignment_rename_content_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('comments', models.TextField(blank=True)),
                ('number', models.CharField(max_length=32, validators=[django.core.validators.RegexValidator('^\\+?[0-9A-D\\#\\*]*$', 'Numbers can only contain: leading +, digits 0-9; chars A, B, C, D; # and *')])),
                ('status', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('forward_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forward_to_set', to='phone.number')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='provider_set', to='circuits.provider')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='region_set', to='dcim.region')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenancy.tenant')),
            ],
            options={
                'verbose_name': 'number',
                'verbose_name_plural': 'numbers',
                'ordering': ('number',),
                'unique_together': {('number', 'tenant')},
            },
        ),
        migrations.CreateModel(
            name='NumberRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'number role',
                'verbose_name_plural': 'number roles',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='VoiceCircuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('voice_circuit_type', models.CharField(max_length=50)),
                ('provider_circuit_id', models.CharField(blank=True, max_length=50)),
                ('sip_source', models.CharField(blank=True, max_length=255)),
                ('sip_target', models.CharField(blank=True, max_length=255)),
                ('assigned_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('assigned_object_type', models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(models.Q(('app_label', 'dcim'), ('model', 'interface')), models.Q(('app_label', 'virtualization'), ('model', 'vminterface')), _connector='OR')), null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='contenttypes.contenttype')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vc_provider_set', to='circuits.provider')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vc_region_set', to='dcim.region')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vc_site_set', to='dcim.site')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenancy.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NumberAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('object_id', models.PositiveBigIntegerField()),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assignments', to='phone.number')),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assignments', to='phone.numberrole')),
            ],
            options={
                'verbose_name': 'number assignment',
                'verbose_name_plural': 'number assignments',
                'ordering': ('number',),
                'indexes': [models.Index(fields=['object_type', 'object_id'], name='phone_numbe_object__560fde_idx')],
            },
        ),
    ]