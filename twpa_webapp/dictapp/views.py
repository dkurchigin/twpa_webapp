from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import DictWithRules
from django.urls import reverse_lazy


class DictListUpdateView(UpdateView):
    model = DictWithRules
    template_name = 'dictapp/rule_list.html'
    fields = ('content',)

    def get_context_data(self, **kwargs):
        context = super(DictListUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Состояния с фразами"
        all_rules = DictWithRules.objects.all()
        context['all_rules'] = all_rules

        rule_number = self.kwargs.get('pk')
        if rule_number:
            concrete_rule = DictWithRules.objects.filter(pk=rule_number).first()
        else:
            concrete_rule = DictWithRules.objects.filter(pk=0).first()
        context['concrete_rule'] = concrete_rule
        return context

    def get_success_url(self):
        return_to = self.kwargs.get('pk')
        return reverse_lazy('dictapp:concrete_rule', kwargs={'pk': return_to})
