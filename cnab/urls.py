from django.urls import path
from . import views 


urlpatterns = [    
    path('', views.home, name='home'),
    path('handle_file', views.handle_file, name='handle_file')    
]
