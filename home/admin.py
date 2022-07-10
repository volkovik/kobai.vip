from django.contrib import admin
from django.utils.html import format_html, escape

from home.models import Link, Post, LinkOnPost


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]
    readonly_fields = ["icon_preview"]

    def icon_preview(self, object: Link):
        return format_html(f'<img width="64" height="64" src="{escape(object.icon.url)}" style="filter: invert(1);">')


class LinkOnPostInline(admin.TabularInline):
    model = LinkOnPost
    verbose_name = "Link"
    verbose_name_plural = "Links"
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [LinkOnPostInline]
    list_display = ["image_preview_short", "creation_date"]
    readonly_fields = ["image_preview"]

    def image_preview(self, object: Post):
        return format_html(f'<img height="256" src="{escape(object.image.url)}">')

    def image_preview_short(self, object: Post):
        return format_html(f'<img height="100" src="{escape(object.image.url)}">')

    image_preview_short.short_description = "Image"
