import unittest
from .source import calcul

l = [(3,4),(5.6,6),(1.2,2.3)]

class TestCalculSimple(unittest.TestCase):
    def test_add(self):
        for a,b in l:
            with self.subTest(a=a,b=b):
                self.assertEqual(calcul.addition(a, b), a + b)

    def test_sous(self):
        for a, b in l:
            with self.subTest(a=a, b=b):
                self.assertEqual(calcul.soustraction(a, b), a - b)

    def test_div(self):
        for a, b in l:
            with self.subTest(a=a, b=b):
                self.assertEqual(calcul.division(a, b), a / b)

    def test_mul(self):
        for a, b in l:
            with self.subTest(a=a, b=b):
                self.assertEqual(calcul.multiplication(a, b), a * b)


class TestCalculComb(unittest.TestCase):
    def test_add_and_sub(self):
        for a,b in l:
            with self.subTest(a=a,b=b):
                self.assertEqual(calcul.addition(calcul.soustraction(a, b), calcul.soustraction(b, a)), (a - b) + (b - a))

