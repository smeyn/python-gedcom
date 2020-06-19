import unittest
from gedcom.parser import Parser
from gedcom.element.element import Element
from gedcom.element.object import ObjectElement
import gedcom.tags


class TestIndividualMethods(unittest.TestCase):

    def setUp(self):
        gedcom_parser = Parser()
        file_path = 'tests/files/Musterstammbaum.ged'
        gedcom_parser.parse_file(file_path)
        self.parser = gedcom_parser
        self.root = gedcom_parser.get_root_element()
        self.child_elements = gedcom_parser.get_root_child_elements()

    def test_find_id(self):

        e1 = self.child_elements[0]
        found = e1.find('@10@')
        self.assertEqual('@10@', found.pointer)

    def test_parent(self):
        e1 = self.child_elements[1]
        found = e1.parents
        self.assertIsNotNone(found)

    def test_siblings(self):
        e1 = self.child_elements[1]
        found = e1.siblings
        self.assertIsNotNone(found)

    def test_children(self):
        e1 = self.child_elements[1]
        found = e1.children
        self.assertIsNotNone(found)

    def test_match(self):
        result = self.parser.match('surname=Mustereisen:name=Anneliese')
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0].is_individual)

    def test_match_invalid_key(self):
        """an invalid key should result in a value error"""
        with self.assertRaises(ValueError):
            self.parser.match('surname=Mustereisen:given_name=Anneliese')
