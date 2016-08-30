# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 01:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=256)),
                ('updated', models.DateTimeField()),
                ('summary', models.TextField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256, unique=True)),
                ('link', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('pubdate', models.DateTimeField(blank=True, null=True, verbose_name='Date of publication')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserEpisode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_new', models.BooleanField(default=True)),
                ('favorite', models.BooleanField(default=False)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Episode')),
            ],
        ),
        migrations.CreateModel(
            name='UserFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.BooleanField(default=False)),
                ('silent', models.BooleanField(default=False)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Feed')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeds', models.ManyToManyField(blank=True, null=True, to='core.Feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='feeds',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Feed'),
        ),
    ]
