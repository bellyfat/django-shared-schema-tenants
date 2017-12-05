# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared_schema_tenants_custom_data', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tenantspecificfieldcharpivot',
            index=models.Index(fields=['tenant'], name='shared_sche_tenant__74d1cd_idx'),
        ),
        migrations.AddIndex(
            model_name='tenantspecificfielddatepivot',
            index=models.Index(fields=['tenant'], name='shared_sche_tenant__3a1328_idx'),
        ),
        migrations.AddIndex(
            model_name='tenantspecificfielddatetimepivot',
            index=models.Index(fields=['tenant'], name='shared_sche_tenant__6449f3_idx'),
        ),
        migrations.AddIndex(
            model_name='tenantspecificfieldfloatpivot',
            index=models.Index(fields=['tenant'], name='shared_sche_tenant__d889c7_idx'),
        ),
        migrations.AddIndex(
            model_name='tenantspecificfieldintegerpivot',
            index=models.Index(fields=['tenant'], name='shared_sche_tenant__a6005f_idx'),
        ),
        migrations.AddIndex(
            model_name='tenantspecificfieldtextpivot',
            index=models.Index(fields=['tenant'], name='shared_sche_tenant__80970f_idx'),
        ),
        migrations.AddIndex(
            model_name='tenantspecifictablespermission',
            index=models.Index(fields=['tenant'], name='shared_sche_tenant__d8a2bb_idx'),
        ),
        migrations.AddIndex(
            model_name='tenantspecifictablesrelationship',
            index=models.Index(fields=['tenant'], name='shared_sche_tenant__d7bba8_idx'),
        ),
    ]