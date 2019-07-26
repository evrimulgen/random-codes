# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 14:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180418_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_followships', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='followship',
            unique_together=set([('follower', 'followed')]),
        ),
    ]