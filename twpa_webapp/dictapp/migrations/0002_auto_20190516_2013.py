# Generated by Django 2.2 on 2019-05-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictwithrules',
            name='created_from',
            field=models.TextField(blank=True, null=True, verbose_name='Название файла'),
        ),
        migrations.AddField(
            model_name='dictwithrules',
            name='was_created_manual',
            field=models.BooleanField(default=True, verbose_name='Словарь создан вручную?'),
        ),
    ]