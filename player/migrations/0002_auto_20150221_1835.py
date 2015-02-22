# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEpisode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_new', models.BooleanField(default=True)),
                ('favorite', models.BooleanField(default=False)),
                ('episode', models.ForeignKey(to='player.Episode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favorite', models.BooleanField(default=False)),
                ('silent', models.BooleanField(default=False)),
                ('episode', models.ForeignKey(to='player.Feed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='episode',
            name='is_new',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='silent',
        ),
    ]
