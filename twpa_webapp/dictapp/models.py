from django.db import models


class DictWithRules(models.Model):
    class Meta:
        verbose_name = 'Словарь правил'
        verbose_name_plural = 'Словари с правилами'

    name = models.CharField(verbose_name='Имя словаря', max_length=255, unique=True)
    content = models.TextField(verbose_name='Правила в словаре', blank=True, null=True)
    was_created_manual = models.BooleanField(verbose_name='Словарь создан вручную?', default=True)
    created_from = models.TextField(verbose_name='Название файла', blank=True, null=True)

    def __str__(self):
        return "{} | {}".format(self.name, self.created_from)
