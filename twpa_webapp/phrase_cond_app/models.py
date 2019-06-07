from django.db import models
from dictapp.models import DictWithRules


class PhrasesCondition(models.Model):
    class Meta:
        verbose_name = 'Состояние с фразами'
        verbose_name_plural = 'Состояния с фразами'

    name = models.CharField(verbose_name='Имя состояния с правилами', max_length=255, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class PhraseBlock(models.Model):
    class Meta:
        verbose_name = 'Блок с фразами'
        verbose_name_plural = 'Блоки с фразами'

    basic_phrase = models.CharField(verbose_name='Базовая фраза', max_length=255, blank=False, null=False)
    phrase_condition = models.ForeignKey(PhrasesCondition, verbose_name='', on_delete=models.CASCADE, related_name='phrase_condition')
    phrases_parts = models.ManyToManyField(DictWithRules, related_name='phrases_parts')
    phrases_parts_exclude = models.ManyToManyField(DictWithRules, related_name='phrases_parts_exclude')

    def __str__(self):
        return "{} IN {}".format(self.basic_phrase, self.phrase_condition)
