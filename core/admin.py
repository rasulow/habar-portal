from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from . import models


admin.site.register(models.Category)
@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'formatted_created_at', 'updated_at')
    list_filter = (('created_at', DateFieldListFilter), 'category__title',)
    search_fields = ('title', 'description')
    
    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M") if obj.created_at else None

    formatted_created_at.short_description = 'Doran wagty  '
    
admin.site.register(models.Weather)
admin.site.register(models.Icons)
