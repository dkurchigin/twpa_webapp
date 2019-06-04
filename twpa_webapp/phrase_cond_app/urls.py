from django.urls import path
import phrase_cond_app.views as phrase_cond_app

app_name = 'phrase_cond_app'

urlpatterns = [
    path('', phrase_cond_app.PhraseCondListView.as_view(), name='index'),
    path('<int:pk>/', phrase_cond_app.BlocksInCondListView.as_view(), name='concrete_phrase_cond'),
    # path('load_json', dictapp.load_json, name='load_json')
]
