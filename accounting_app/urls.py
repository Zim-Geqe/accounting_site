from django.urls import path
from accounting_app.views import landing
from django.urls import path, include
urlpatterns = [
  
    path('', landing, name='landing'),

]