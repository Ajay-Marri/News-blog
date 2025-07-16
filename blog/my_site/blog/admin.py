from django.contrib import admin
from .models import author, Tag, post

# Register your models here.

class postadmin(admin.ModelAdmin):
    list_filter=("author","tag","date")
    list_display=("title","date","author")
    prepopulated_fields={"slug":("title",)}

admin.site.register(post,postadmin)
admin.site.register(author)
admin.site.register(Tag)