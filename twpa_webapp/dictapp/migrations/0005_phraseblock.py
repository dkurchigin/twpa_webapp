# Generated by Django 2.2 on 2019-06-01 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0004_phrasescondition'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhraseBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_phrase', models.CharField(max_length=255, verbose_name='Базовая фраза')),
                ('phrase_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phrase_condition', to='dictapp.PhrasesCondition', verbose_name='')),
            ],
            options={
                'verbose_name': 'Блок с фразами',
                'verbose_name_plural': 'Блоки с фразами',
            },
        ),
    ]
