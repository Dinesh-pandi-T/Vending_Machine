from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customize/<str:name>/', views.customize, name='customize'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]
