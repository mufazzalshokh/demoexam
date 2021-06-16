from django.contrib import admin

from home.models import NewsModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'created_at']
