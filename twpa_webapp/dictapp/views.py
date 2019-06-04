from django.shortcuts import render
from django.views.generic.list import ListView
from .models import DictWithRules


class DictListView(ListView):
    model = DictWithRules
    template_name = 'dictapp/rule_list.html'

    # def get_queryset(self):
    #     qs = super(DictListView, self).get_queryset()
    #     condition = self.kwargs.get('pk')
    #     print(condition)
    #     if condition:
    #         return qs
    #     else:
    #         return

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DictListView, self).get_context_data(**kwargs)
        context['title'] = "Состояния с фразами"

        rule_number = self.kwargs.get('pk')
        if rule_number:
            concrete_rule = DictWithRules.objects.filter(pk=rule_number).first()
        else:
            concrete_rule = DictWithRules.objects.filter(pk=0).first()
        context['concrete_rule'] = concrete_rule
        print(context)
        return context
