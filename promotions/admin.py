from django.contrib import admin
from .models import Promo, NewsLetter
from django_summernote.admin import SummernoteModelAdmin

class NewsletterAdmin(SummernoteModelAdmin):
    fields = ['message']
    summernote_fields = ('message',)

admin.site.register(Promo)
admin.site.register(NewsLetter, NewsletterAdmin)

