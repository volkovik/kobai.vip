from django.contrib import admin
from django.utils.html import format_html, escape
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableInlineAdminMixin

from home.models import Link, Post, PostLink, PostImage


def image_html(source: str, **kwargs) -> str:
    """Generate a image HTML tag (<img/>)"""
    params = [f'src="{escape(source)}"'] + [f'{key}="{value}"' for key, value in kwargs.items()]
    return format_html(f"<img {' '.join(params)}/>")


@admin.register(Link)
class LinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Admin model for links"""

    list_display = ["name", "thumbnail_column", "url"]
    readonly_fields = ["thumbnail_field"]

    def thumbnail_field(self, link: Link) -> str:
        """Icon preview field"""
        return image_html(link.icon.url, width=64, height=64)
    thumbnail_field.short_description = "Preview"

    def thumbnail_column(self, link: Link) -> str:
        """Icon preview in list as a category"""
        return image_html(link.icon.url, width=16, height=16)
    thumbnail_column.short_description = "Preview"


@admin.register(Post)
class PostAdmin(SortableAdminBase, admin.ModelAdmin):
    class PostImageInline(SortableInlineAdminMixin, admin.StackedInline):
        """Inline admin model for images of post"""

        model = PostImage
        verbose_name = "Image"
        verbose_name_plural = "Images"

        extra = 0
        min_num = 1
        max_num = 10

        readonly_fields = ["thumbnail"]

        def thumbnail(self, post_image: PostImage) -> str:
            """Image preview field"""
            return image_html(post_image.image.url, height=256)

    class PostLinkInline(SortableInlineAdminMixin, admin.TabularInline):
        """Inline admin model for links of post"""

        model = PostLink
        verbose_name = "Link"
        verbose_name_plural = "Links"

        extra = 0
        min_num = 0
        max_num = 10

    inlines = [PostImageInline, PostLinkInline]
    list_display = ["thumbnail_column", "title", "creation_date"]

    def thumbnail_column(self, post: Post) -> str:
        post_image = post.image.order_by("order").first()
        if post_image is not None:
            return image_html(post_image.image.url, height=128)
        else:
            return ""
    thumbnail_column.short_description = "Preview"
