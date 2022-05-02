from django.contrib import admin
from .models import Promo

class PromotionsAdminArea(admin.AdminSite):
    site_header = "Promotions Admin"

promotions_site= PromotionsAdminArea(name='PromotionsAdmin')

promotions_site.register(Promo)
admin.site.register(Promo)

