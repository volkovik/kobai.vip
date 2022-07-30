from django.contrib import admin
from django.utils.html import format_html, escape
from adminsortable2.admin import SortableAdminMixin

from home.models import Link, Post, PostLink


@admin.register(Link)
class LinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["name", "url"]
    readonly_fields = ["icon_preview"]

    def icon_preview(self, link: Link) -> str:
        return format_html(f'<img width="64" height="64" src="{escape(link.icon.url)}" style="filter: invert(1);">')


class PostLinkInline(admin.TabularInline):
    model = PostLink
    verbose_name = "Link"
    verbose_name_plural = "Links"
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostLinkInline]
    list_display = ["image_preview_short", "creation_date"]
    readonly_fields = ["image_preview"]

    def image_preview(self, post: Post) -> str:
        return format_html(f'<img height="256" src="{escape(post.image.url)}">')

    def image_preview_short(self, post: Post) -> str:
        return format_html(f'<img height="100" src="{escape(post.image.url)}">')

    image_preview_short.short_description = "Image"
