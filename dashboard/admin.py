from django.contrib import admin

from .models import Profile, Message, Wishlist

admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Wishlist)