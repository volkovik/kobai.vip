from django.contrib import admin

from home.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]
