from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('id', 'email', )
    readonly_fields = ('password', )


admin.site.register(Account, AccountAdmin)
