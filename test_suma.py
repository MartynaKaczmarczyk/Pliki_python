import unittest
from suma.py import suma

class TestSuma(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum(0, 2), 2)
        self.assertEqual(sum(4, 5), 9)
        self.assertEqual(sum(-2, -1), -3)
        
if __name__ == '__main__':
    unittest.main()
