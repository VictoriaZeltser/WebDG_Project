

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Передаем ссылку на функцию, а не вызываем её
    path('data/', views.data, name='data'),
    path('test/', views.test, name='test'),
]

