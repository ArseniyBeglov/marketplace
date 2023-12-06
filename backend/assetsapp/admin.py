from django.contrib import admin
from . import models


class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'version', 'archived', 'asset_link', 'images_link')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'version', 'asset_link')



admin.site.register(models.Asset, AssetAdmin)