from django.contrib import admin
from django.utils.html import format_html

from home.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]
    readonly_fields = ["icon_preview"]


    def icon_preview(self, object: Link):
        from django.utils.html import escape

        return format_html('<img width="64" height="64" src="{}" style="filter: invert(1);"></i>'.format(
            escape(object.icon.url))
        )
