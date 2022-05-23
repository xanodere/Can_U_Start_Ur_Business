from django.contrib import admin
from main.models import cache, Site


class CacheAdmin(admin.ModelAdmin):
    list_display = ["Activité", "Competitivité"]


admin.site.register(cache, CacheAdmin)
admin.site.register(Site)