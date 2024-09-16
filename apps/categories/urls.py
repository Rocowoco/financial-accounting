from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
]
