from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PhrasesCondition, PhraseBlock
from django.urls import reverse_lazy
from dictapp.models import DictWithRules


class PhraseCondListView(ListView):
    model = PhrasesCondition
    template_name = 'phrase_cond_app/base.html'

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

        context['condition'] = block_name
        context['title'] = f"Блок - {block_name}"

        phrase_blocks = PhraseBlock.objects.filter(phrase_condition=block_name.pk)
        phrases_parts = {}
        phrases_parts_exclude = {}
        phrases_exact = {}
        next_state = {}

        for block in phrase_blocks:
            # print(block.pk)
            parts_block = DictWithRules.objects.filter(phrases_parts=block.pk)
            phrases_parts[block.pk] = parts_block
            parts_exclude_block = DictWithRules.objects.filter(phrases_parts_exclude=block.pk)
            phrases_parts_exclude[block.pk] = parts_exclude_block
            exact_block = DictWithRules.objects.filter(phrases_exact=block.pk)
            phrases_exact[block.pk] = exact_block
            next_state[block.pk] = block.next_state

        context['phrases_parts_for_block'] = phrases_parts
        context['phrases_parts_exclude_for_block'] = phrases_parts_exclude
        context['phrases_exact_for_block'] = phrases_exact
        context['next_state_for_block'] = next_state
        # print(context)

        return context


class PhraseBlockDeleteView(DeleteView):
    model = PhraseBlock
    template_name = 'phrase_cond_app/phrase_block_delete.html'

    def get_context_data(self, **kwargs):
        context = super(PhraseBlockDeleteView, self).get_context_data(**kwargs)
        block_name = context['object'].basic_phrase
        context['title'] = f'Удалить блок \"{block_name}\"'
        return context

    def get_success_url(self):
        return_to = self.request.POST.get('from_condition')
        return reverse_lazy('phrase_cond_app:concrete_phrase_cond', kwargs={'pk': return_to})


class PhraseBlockUpdateView(UpdateView):
    model = PhraseBlock
    template_name = 'phrase_cond_app/phrase_block_update.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PhraseBlockUpdateView, self).get_context_data(**kwargs)
        block_name = context['object'].basic_phrase
        context['title'] = f'Редактировать блок \"{block_name}\"'
        return context

    def get_success_url(self):
        return_to = self.request.POST.get('from_condition')
        return reverse_lazy('phrase_cond_app:concrete_phrase_cond', kwargs={'pk': return_to})
