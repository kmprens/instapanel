from django.contrib import admin
from .models import  Insta

class PostAdmin(admin.ModelAdmin):
    list_display = ['kuladi','takipci', 'takip','paylasim','kaydetmetarihi','prikuladi']
    list_display_links=['kuladi']
    list_filter=['kaydetmetarihi']
    search_fields=['kuladi','kaydetmetarihi']


    class meta:
        model = Insta

admin.site.register(Insta,PostAdmin)


