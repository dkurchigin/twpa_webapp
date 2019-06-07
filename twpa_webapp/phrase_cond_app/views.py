from django.shortcuts import render
from django.views.generic.list import ListView
from .models import PhrasesCondition, PhraseBlock
from dictapp.models import DictWithRules


class PhraseCondListView(ListView):
    model = PhrasesCondition
    template_name = 'phrase_cond_app/base.html'

    # def get_queryset(self):
    #     qs = super(PhraseCondListView, self).get_queryset()
    #     condition = self.kwargs.get('pk')
    #     print(condition)
    #     if condition:
    #         self.template_name = 'phrase_cond_app/condition.html'
    #         return qs
    #     else:
    #         return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PhraseCondListView, self).get_context_data(**kwargs)
        context['title'] = "Состояния с фразами"
        return context


class BlocksInCondListView(ListView):
    model = PhraseBlock
    template_name = 'phrase_cond_app/condition.html'

    def get_queryset(self):
        qs = super(BlocksInCondListView, self).get_queryset()
        condition = self.kwargs.get('pk')
        return qs.filter(phrase_condition=condition)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlocksInCondListView, self).get_context_data(**kwargs)
        condition = self.kwargs.get('pk')
        block_name = PhrasesCondition.objects.filter(pk=condition).first()
        context['title'] = "{} - блоки".format(block_name)

        phrase_blocks = PhraseBlock.objects.filter(phrase_condition=block_name.pk)
        phrases_parts = {}
        phrases_parts_exclude = {}
        for block in phrase_blocks:
            print(block.pk)
            parts_block = DictWithRules.objects.filter(phrases_parts=block.pk)
            phrases_parts[block.pk] = parts_block
            parts_exclude_block = DictWithRules.objects.filter(phrases_parts_exclude=block.pk)
            phrases_parts_exclude[block.pk] = parts_exclude_block
        context['phrases_parts_for_block'] = phrases_parts
        context['phrases_parts_exclude_for_block'] = phrases_parts_exclude
        print(context)

        return context
