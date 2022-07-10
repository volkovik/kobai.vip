from os import path
from django.core.exceptions import ValidationError

from django.test import TestCase
from django.core.files import File

from .models import Link


class LinkIconTestCase(TestCase):
    """This test case checking SVG file validation of icon field in Link django model"""

    DIR_PATH = "static/tests/home/link_icon"  # Test files of the tests

    def create_and_validate_example_model(self, file_name: str) -> None:
        with open(path.join(self.DIR_PATH, file_name), "rb") as file:
            link = Link.objects.create(
                name="Example",
                url="https://example.com/",
                icon=File(file, name=file.name) 
            )
            link.full_clean()

    def test_svg_file(self) -> None:
        self.create_and_validate_example_model("triangle.svg")
    
    def test_jpg_file(self) -> None:
        with self.assertRaises(ValidationError):
            self.create_and_validate_example_model("triangle.jpg")

    def test_blank_svg_file(self) -> None:
        with self.assertRaises(ValidationError):
            self.create_and_validate_example_model("blank.svg")
    
    def test_invalid_svg_file(self) -> None:
        with self.assertRaises(ValidationError):
            self.create_and_validate_example_model("invalid.svg")
