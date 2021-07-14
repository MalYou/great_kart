from django.contrib import admin

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description', 'image', ) 
    list_display_links = ('id', 'slug')
    prepopulated_fields = {
        'slug': ('name', )
    }


admin.site.register(Category, CategoryAdmin)
