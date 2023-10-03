from django.urls import path

from viagens import views

app_name = 'viagens'

urlpatterns = [
    path("", views.index, name='index'),
    path("search/", views.search, name='search'),

    # viagens (CRUD)
    path("viagens/<int:viagem_id>/detail/", views.viagem, name='viagem'),
    path("viagens/create/", views.create, name='create'),
    # path("viagens/<int:viagem_id>/update/", views.viagem, name='viagem'),
    # path("viagens/<int:viagem_id>/delete/", views.viagem, name='viagem'),
]
