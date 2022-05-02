from django.contrib import admin
from .models import Category, Product, Review
from promotions.models import Promo
from orders.models import Order


class StoreAdminArea(admin.AdminSite):
    site_header = "Ebiblio Store Administration"
    index_title = "E-biblio Store Administration"
    site_title = "Admin"


class StoreProductAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'category', 'image', 'pdf', 'price']


store_site=StoreAdminArea(name='store_admin')

store_site.register(Product, StoreProductAdmin)
# store_site.register(Product)
store_site.register(Order)
store_site.register(Promo)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated']
    list_filters = ['in_stock']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Review)
