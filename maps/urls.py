from . import views
from django.urls import path

urlpatterns = [
    path('', views.show, name='maps'),
    path('search/', views.search, name='search'),
    path('/', views.home, name='home')
]


