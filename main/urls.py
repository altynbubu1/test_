from django.urls import path
from . import views


urlpatterns = [
    path('employee/', views.home, name='home'),
    path('success/', views.success, name='success'),
]