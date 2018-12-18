import unittest

from os import path
from gedcom.gedcom import Gedcom

here = path.abspath(path.dirname(__file__))
test_files = path.join(here, 'test_files/')


class TestGedcom(unittest.TestCase):

    def setUp(self):
        self.gedcom = Gedcom(path.join(test_files, 'Mustermann.ged'))

    def test_parses_successfully(self):
        assert len(self.gedcom.get_element_list()) == 376
