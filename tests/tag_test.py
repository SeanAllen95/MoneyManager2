import unittest

from models.tag import Tag

class TestTag(unittest.TestCase):
    def setUp(self):
        self.tag = Tag("Clothing")

    def test_tag_has_category(self):
        self.assertEqual("Clothing", self.tag.category)
    