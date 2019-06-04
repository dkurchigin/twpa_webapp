from django.urls import path
import dictapp.views as dictapp

app_name = 'dictapp'

urlpatterns = [
    path('', dictapp.DictListView.as_view(), name='index'),
    path('<int:pk>/', dictapp.DictListView.as_view(), name='concrete_rule'),
    # path('<int:pk>/', dictapp.BlocksInCondListView.as_view(), name='concrete_phrase_cond'),
    # path('load_json', dictapp.load_json, name='load_json')
]
