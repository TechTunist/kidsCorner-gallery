from django.urls import path
from . import views


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('image/<str:pk>/', views.viewImage, name='image'),
    path('add/', views.addImage, name='add'),

]