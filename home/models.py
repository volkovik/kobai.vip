import re
from django.core.exceptions import ValidationError
from django.db import models


def validate_svg_file(file: models.FileField) -> None:
    """Validating SVG files for FileField in django models"""
    
    # Checking filetype in name of the file
    if file.name.split(".")[-1] != "svg":
        raise SVGValidationError()

    # Checking data structure of the file
    svg_regex = re.compile(r"(?:<\?xml\b[^>]*>[^<]*)?(?:<!--.*?-->[^<]*)*(?:<svg|<!DOCTYPE svg)\b", re.DOTALL)
    file_data = file.file.read().decode("latin_1")

    if svg_regex.match(file_data) is None:
        raise SVGValidationError()


class SVGValidationError(ValidationError):
    """Custom exception class for non-SVG type files"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__("File must be SVG type", *args, **kwargs)


class Link(models.Model):
    """Django model for social & media links"""

    name = models.CharField(max_length=32, unique=True)
    url = models.URLField(verbose_name="URL")
    icon = models.FileField(
        upload_to="images/links/",
        help_text="Only SVG files. The image will be used to show links on home page",
        validators=[validate_svg_file]
    )

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    """Django model for works of portfolio"""

    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to="images/posts/")
    description = models.TextField(max_length=256)
    creation_date = models.DateField()

    def __str__(self) -> str:
        return f"Post of {self.creation_date}"
    

class PostLink(models.Model):
    """Django model for links that are related to post"""

    post = models.ForeignKey(Post, related_name="link", on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    url = models.URLField(verbose_name="URL")
