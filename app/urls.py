"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from kafe_id.views import tampilkan_menu, proses_pesanan, Dashboard_admin, update_status_pesanan
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', Dashboard_admin, name='dashboard_admin'),
    path('dashboard/update/<int:pesanan_id>/<str:status_baru>/', update_status_pesanan, name='update_status'),
    # path('pesanan/<int:id>/<str:status>/', update_status_pesanan, name='update_status'),
    path('meja/<int:id>/', tampilkan_menu, name='tampilkan_menu'),
    path("pesanan/", proses_pesanan, name="proses_pesanan"),
]

# Tambahkan URL untuk media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)