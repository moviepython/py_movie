from django.urls import path
from .import views

urlpatterns =[
    path('', views.store, name='store'),
    path('detail_view/<int:id>/', views.detail_view, name='detail_view'),
    path('<slug:movie_slug>/', views.store, name='listmovies_by_movie'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('edit/<int:edit_id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),

]