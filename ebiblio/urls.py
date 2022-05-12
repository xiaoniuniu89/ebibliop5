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
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('promotions/', include('promotions.urls', namespace='promotions')),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('privacy-policy/', TemplateView.as_view(
        template_name='privacy_policy.html'), name='privacy_policy'),
    path('cookie-policy/', TemplateView.as_view(
        template_name='cookie_policy.html'), name='cookie_policy')

]

admin.site.index_title = "E-biblio"
admin.site.site_header = "E-biblio Admin"
admin.site.site_title = "Admin"

# error handle pages
# page not found
# handler404 = 'store.views.handle_404'
# server error
handler500 = 'store.views.handle_500'
# permission error
handler403 = 'store.views.handle_403'
# bad request error
handler400 = 'store.views.handle_400'

