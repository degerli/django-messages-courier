# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-04 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0003_notificationprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='NotificationProfile',
        ),
    ]
