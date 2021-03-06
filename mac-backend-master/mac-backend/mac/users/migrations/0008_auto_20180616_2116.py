# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-16 18:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mac.users.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_make_skill_float'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, unique=True)),
                ('until', models.DateTimeField(default=mac.users.utils.twentyfour_hours)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='until',
            field=models.DateTimeField(default=mac.users.utils.twentyfour_hours),
        ),
    ]
