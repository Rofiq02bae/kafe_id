from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.Dashboard_admin, name='dashboard_admin'),
    path('pesanan/<int:id>/<str:status>/', views.update_status_pesanan, name='update_status'),
    path('meja/<int:id>/', views.tampilkan_menu, name='tampilkan_menu'),
    path('pesan/', views.proses_pesanan, name='proses_pesanan'),
]
# path('pesanan/<int:id>/<str:status>/', views.update_status_pesanan, name='update_status'),
