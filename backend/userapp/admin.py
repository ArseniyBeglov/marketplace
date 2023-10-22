from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_seller', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'username')
    search_fields = ('id', 'username', 'email')


admin.site.register(MyUser, MyUserAdmin)