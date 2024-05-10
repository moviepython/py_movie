from django.urls import path
from .import views

urlpatterns =[
    path('review/add/<int:id>/', views.review_add, name='review_add'),
]