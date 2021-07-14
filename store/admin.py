from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'price', 'stock', 'is_available', 'created_date',)
    list_display_links = ('id', 'slug',)
    ordering = ('id', 'created_date',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Product, ProductAdmin)
