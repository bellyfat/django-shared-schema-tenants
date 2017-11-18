# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 01:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import shared_schema_tenants.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('shared_schema_tenants', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shared_schema_tenants_custom_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantSpecificTablesGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tenant_specific_table_group', to='auth.Group')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'original_manager',
                'default_manager_name': 'original_manager',
            },
            managers=[
                ('original_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TenantSpecificTablesPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants_custom_data.TenantSpecificTable')),
                ('tenant', models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'original_manager',
                'default_manager_name': 'original_manager',
            },
            managers=[
                ('original_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TenantSpecificTablesRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.ManyToManyField(related_name='relationships', to='shared_schema_tenants_custom_data.TenantSpecificTablesGroup')),
                ('permissions', models.ManyToManyField(related_name='relationships', to='shared_schema_tenants_custom_data.TenantSpecificTablesPermission')),
                ('tenant', models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'original_manager',
                'default_manager_name': 'original_manager',
            },
            managers=[
                ('original_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='tenantspecifictablesgroup',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='shared_schema_tenants_custom_data.TenantSpecificTablesPermission'),
        ),
        migrations.AddField(
            model_name='tenantspecifictablesgroup',
            name='tenant',
            field=models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant'),
        ),
    ]
