# Generated by Django 2.1 on 2018-08-25 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='rank',
        ),
    ]