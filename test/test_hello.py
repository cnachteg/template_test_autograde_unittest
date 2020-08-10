import unittest
from .source import hello


class TestHello(unittest.TestCase):
    def test_string(self):
        self.assertEqual(hello.hello('Charlotte'), "Hello Charlotte !", msg="Ooops, this is not the right message !")