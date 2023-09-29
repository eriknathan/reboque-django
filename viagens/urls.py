from django.urls import path

from viagens import views

app_name = 'viagens'

urlpatterns = [
    path("", views.index, name='index'),
]
