# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-05 15:41
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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0434\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('content', models.TextField(verbose_name='\u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u0430\u0432\u0442\u043e\u0440')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0441\u0442',
                'verbose_name_plural': '\u041f\u043e\u0441\u0442\u044b',
            },
        ),
    ]
