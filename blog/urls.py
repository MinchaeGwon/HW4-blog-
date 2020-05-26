from django.urls import path
from . import views

urlpatterns = [
    path('newblog/', views.create, name="newblog"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('<int:blog_id>', views.detail, name="detail"),
    path('new/', views.new, name='new'),
]