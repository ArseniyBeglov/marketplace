from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'fio', 'email', 'sex', 'about', 'is_seller')
    search_fields = ('id', 'username', 'email', 'fio')
    list_display_links = ('id', 'username', 'email', 'fio')


admin.site.register(MyUser, MyUserAdmin)