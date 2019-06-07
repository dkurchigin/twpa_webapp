# Generated by Django 2.2 on 2019-06-07 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0008_remove_dictwithrules_use_in_block'),
        ('phrase_cond_app', '0008_auto_20190602_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='phraseblock',
            name='phrases_parts_exclude',
            field=models.ManyToManyField(related_name='phrases_parts_exclude', to='dictapp.DictWithRules'),
        ),
    ]