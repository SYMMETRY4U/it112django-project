from django.urls import path
from . import views
from .views import InventionListView, InventionDetailView

urlpatterns = [
  path("", views.HomeView.as_view(), name='home_view'),
  path('about/', views.AboutView.as_view(), name='about_view'),
  path('function/', views.FunctionView.as_view(), name='function_view'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('cr250/', views.Cr250View.as_view(), name='cr250'),
  path('yz125/', views.Yz125View.as_view(), name='yz125'),
  path('noguchi/', views.NoguchiView.as_view(), name='noguchi'),
  path('motocross/', views.MotocrossView.as_view(), name='motocross'),
  path('load/', views.load_default_data_view, name='load_default_data'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
  path('inventions/', InventionListView.as_view(), name='invention-list'),
  path('invention/<int:pk>/', InventionDetailView.as_view(), name='invention-view'),
  # more urls?

  ]
