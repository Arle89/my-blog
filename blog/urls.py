from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name="index.html"),
    path('índex.html', views.post_list),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),

    
]
