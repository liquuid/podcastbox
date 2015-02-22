# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=256)),
                ('updated', models.DateTimeField()),
                ('summary', models.TextField(max_length=512, null=True, blank=True)),
                ('is_new', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(unique=True, max_length=256)),
                ('link', models.CharField(max_length=256, null=True, blank=True)),
                ('description', models.TextField(max_length=1024, null=True, blank=True)),
                ('title', models.CharField(max_length=64, null=True, blank=True)),
                ('pubdate', models.DateTimeField(null=True, verbose_name=b'Date of publication', blank=True)),
                ('silent', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feeds', models.ManyToManyField(to='player.Feed', null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='episode',
            name='feeds',
            field=models.ForeignKey(to='player.Feed'),
            preserve_default=True,
        ),
    ]
