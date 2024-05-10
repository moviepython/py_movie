from django.urls import path
from .import views
app_name = 'film_app'

urlpatterns = [
    path('', views.movie, name='movie'),

    ]