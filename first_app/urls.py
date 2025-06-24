from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('api/echo/', views.EchoData.as_view(), name='echo-data'),
] 