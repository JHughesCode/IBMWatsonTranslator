import unittest
from translator import e2f
from translator import f2e

class testmyscript(unittest.TestCase):
    def teste2f(self):
        self.assertIn("Bonjour", str(e2f("hello")))

    def test_when_e2f_is_null(self):
        self.assertIsNotNone(e2f("hello"), None)

    def testf2e(self):
        self.assertIn("Hello", str(f2e("bonjour")))

    def test_when_f2e_is_null(self):
        self.assertIsNotNone(f2e("bonjour"), None)

if __name__ == '__main__':
    unittest.main()
