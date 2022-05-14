from django.contrib import admin
from .models import Promo, NewsLetter, Subscriber
from django_summernote.admin import SummernoteModelAdmin

class NewsletterAdmin(SummernoteModelAdmin):
    fields = ['message']
    summernote_fields = ('message',)


class SubAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('email', 'slug_end')}


admin.site.register(Promo)
admin.site.register(Subscriber, SubAdmin)
admin.site.register(NewsLetter, NewsletterAdmin)