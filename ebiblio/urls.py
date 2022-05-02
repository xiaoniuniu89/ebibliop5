"""ebiblio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('promotions/', include('promotions.urls', namespace='promotions')),
    path('accounts/', include('allauth.urls')),
]

admin.site.index_title = "E-biblio"
admin.site.site_header = "E-biblio Admin"
admin.site.site_title = "Admin"


