import unittest
from webserver import fact



class TestFact(unittest.TestCase):
    
     def test_fact(self):
    
        res = fact(-1)
        self.assertEqual(res, -1)
        
        res = fact(0)
        self.assertEqual(res, 1)
        
        res=fact(1)
        self.assertEqual(res, 1)
        
        res = fact(5)
        self.assertEqual(res, 120)
        
        
if __name__ == '__main__':
    unittest.main()
