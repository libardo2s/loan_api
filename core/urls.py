"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from apps.customers.views import CustomerAPIView


api_patterns = [
    path('customers/', CustomerAPIView.as_view(), name='customers-list'),
    path('customers/<int:customer_id>/', CustomerAPIView.as_view(), name='customer-detail'),
]


urlpatterns = [
    path('api/', include(api_patterns)),
    path('admin/', admin.site.urls),
]
