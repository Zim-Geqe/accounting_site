from django.urls import path
from accounting_app.views import landing
from django.urls import path, include
from . import views

urlpatterns = [
  
    path('', landing, name='landing'),
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),


]