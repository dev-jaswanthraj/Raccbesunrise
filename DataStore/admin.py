from django.contrib import admin
from .models import onefitTabel


class listAdmin(admin.ModelAdmin):
    search_fields = ['user_id']

admin.site.register(onefitTabel, listAdmin)
