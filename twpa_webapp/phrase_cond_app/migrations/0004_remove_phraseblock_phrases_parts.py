# Generated by Django 2.2 on 2019-06-01 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phrase_cond_app', '0003_auto_20190601_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phraseblock',
            name='phrases_parts',
        ),
    ]