# Generated by Django 2.2 on 2019-05-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0002_auto_20190516_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictwithrules',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Правила в словаре'),
        ),
    ]
