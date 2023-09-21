from django.test import TestCase
from apps.resources import models


# Test Case class # Test<model-name>Model
class TestTagModel(TestCase):
    def setUp(self)-> None:
        self.tag_name = 'Python'
        self.tag = models.Tag(name=self.tag_name)
        
        
        
            
    # unit test 1# test_<logic-name>
    def test_create_tag_object_successful(self):
        # Check if the object created is of the instance Tag
        self.assertIsInstance(self.tag, models.Tag)
        
    # unit test 2
    def test_dunder_str(self):
       #str(self.tag) or self.tag.__str__()
        self.assertEqual(str(self.tag), self.tag_name)
        
        
class TestCategoryModel(TestCase):
    def setUp(self):
        self.category_name = 'Data Science'
        self.category = models.Category(cat = self.category_name)
        
    def test_create_category_object_successful(self):
        self.assertIsInstance(self.category, models.Category)
        
    def test_category_method__str(self):
        self.assertEqual(str(self.category), self.category_name)
        
    def test_category_meta_verbose_name_plural(self):
        name = "Categories"
        #self.assertEqual(name, models.Category._meta.verbose_name_plural)
        self.assertEqual(name, self.category._meta.verbose_name_plural)