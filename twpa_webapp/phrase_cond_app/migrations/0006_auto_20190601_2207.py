# Generated by Django 2.2 on 2019-06-01 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0008_remove_dictwithrules_use_in_block'),
        ('phrase_cond_app', '0005_phraseblock_phrases_parts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phraseblock',
            name='phrases_parts',
        ),
        migrations.AddField(
            model_name='phraseblock',
            name='phrases_parts',
            field=models.ManyToManyField(to='dictapp.DictWithRules'),
        ),
    ]
