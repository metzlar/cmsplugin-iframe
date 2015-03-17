# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='IFrame',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('width', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('height', models.PositiveSmallIntegerField()),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
