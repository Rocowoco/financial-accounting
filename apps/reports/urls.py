from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReportListView.as_view(), name='report_list'),
    path('<str:report_type>/', views.ReportDetailView.as_view(), name='report_detail'),
]
