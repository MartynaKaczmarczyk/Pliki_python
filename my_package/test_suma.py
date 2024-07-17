import unittest
from .suma import suma

class TestSuma(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(suma(0, 2), 2)
        self.assertEqual(suma(4, 5), 9)
        self.assertEqual(suma(-2, -1), -3)
        
if __name__ == '__main__':
    unittest.main()
