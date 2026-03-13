from django.contrib import admin
from django.urls import path
import myapp.views as views

urlpatterns = [
    path('index', views.home, name='index'),
    path('perform/action', views.perform_action, name='perform_action'),
    path('get/plugins', views.get_plugins, name='get_plugins'),
    path('', views.home, name='home'),        
    path('<path:url>', views.home, name='catch_all'),

]
