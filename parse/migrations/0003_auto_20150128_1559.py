# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0002_auto_20150128_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.TextField()),
                ('url', models.ForeignKey(to='parse.Sites')),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='sites',
            options={'verbose_name_plural': 'Sites'},
        ),
    ]
