import sys
sys.path.append("/alx-higher_level_engineering/0x0C-python-almost_a_circle/models")
import base
import unittest

class test_base(unittest.TestCase):

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base ()
        self.b6 = Base(9)
        self.b6.id = 34
    def test_init(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)
        self.assertEqual(self.b6.id, 34)


if __name__ == "__main__":
    unittest.main()
