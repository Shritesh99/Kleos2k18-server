# Generated by Django 2.1 on 2018-08-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_questionid'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hint1',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='hint2',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='hint3',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='hint4',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]