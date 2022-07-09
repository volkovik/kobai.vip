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
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("File must be SVG type", *args, **kwargs)


class Link(models.Model):
    """Django model for social & media links"""

    name = models.CharField(
        verbose_name="Name",
        unique=True,
        max_length=32
    )
    url = models.URLField(
        verbose_name="URL"
    )
    icon = models.FileField(
        verbose_name="Icon",
        upload_to="images/links/",
        help_text="Only SVG files. The image will be used to show links on home page",
        validators=[validate_svg_file]
    )

    def __str__(self) -> str:
        return self.name
