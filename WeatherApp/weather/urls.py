from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('<int:pk>', views.city_detail,name='city_detail')
]