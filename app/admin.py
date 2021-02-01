from django.contrib import admin

# Register your models here.
from .models import urls,top_words

admin.site.register(urls)

class admintopwords(admin.ModelAdmin):
    list_display=['url','word','frequency']
admin.site.register(top_words,admintopwords)