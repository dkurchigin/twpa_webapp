# Generated by Django 2.2 on 2019-06-01 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phrase_cond_app', '0002_phraseblock_phrases_parts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phraseblock',
            name='phrases_parts',
            field=models.ManyToManyField(default=None, to='dictapp.DictWithRules'),
        ),
    ]