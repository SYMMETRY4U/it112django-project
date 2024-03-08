from django.urls import path
from . import views

urlpatterns = [
  # path("",views.home, name="home"),
  path("", views.HomeView.as_view(), name='home_view'),
  path('about/', views.AboutView.as_view(), name='about_view'),
  path('function/', views.function_view, name='function_view'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
  
]
