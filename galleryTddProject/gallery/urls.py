from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolios/', views.list_portfolios, name='portfolios'),
    path('addUser/', views.add_user_view, name='addUser'),
]
