# Generated by Django 3.0.6 on 2020-05-25 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softlab', '0002_friend_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='nick_name',
        ),
    ]