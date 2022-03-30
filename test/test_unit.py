import unittest
from models import Models
from parameterized import parameterized 

class UnitTests(unittest.TestCase):
    models = None 

    def setUp(self):
        self.models = Models()

    def test_index(self):
        self.assertEqual(self.models.index(), {})

    def test_lists(self):
        self.assertEqual(self.models.index(), {})
        
    @parameterized.expand([
        ("Add to empty list", [], {'items': ["New Item"]}),
        ("Add to list with one item", ["1"], {'items': ["1", "New Item"]}),
        ("Add to list with two items", ["1", "2"], {'items': ["1", "2", "New Item"]}),
        ])
    def test_newItem(self, description, items, expectedResult):
        self.assertEqual(self.models.newItem(items), expectedResult)
 
    @parameterized.expand([
        ("Edit first item", ["1"], 1, {'before': [], 'current': "1", 'after': []}),
        ("Edit second item", ["1", "2"], 2, {'before': ["1"], 'current': "2", 'after': []}),
        ])
    def test_editItem(self, description, items, itemId, expectedResult):
        self.assertEqual(self.models.editItem(items, 0, itemId), expectedResult)

    @parameterized.expand([
         ("Save item empty list", []), 
         ("Save item single item list", ['asdfasf']), 
         ("Save item two items list", ['asdfasf', 'sadfasdf']), 
        ])
    def test_saveItem(self, description, items):
        self.assertEqual(self.models.saveItem(items, 0, 0), {'items': items})
 
