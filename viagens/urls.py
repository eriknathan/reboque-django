from django.urls import path

from viagens import views

app_name = 'viagens'

urlpatterns = [
    path("<int:viagem_id>/", views.viagem, name='viagem'),
    path("search/", views.search, name='searchtá jogando'),
    path("", views.index, name='index'),
]
