from django.contrib import admin
from app.models import Content

# Register your models here.
class ListContent(admin.ModelAdmin):
    list_display = ('title', 'text')

admin.site.register(Content, ListContent)