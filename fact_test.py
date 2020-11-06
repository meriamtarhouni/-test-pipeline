import unittest
import timeit
from webserver import fact,fact_Iterative



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
        
    def test_fact_iterative(self):
        
        res = fact_Iterative(-1)
        self.assertEqual(res, -1)
        
        res = fact_Iterative(0)
        self.assertEqual(res, 1)
        
        res= fact_Iterative(1)
        self.assertEqual(res, 1)
        
        res = fact_Iterative(5)
        self.assertEqual(res, 120)



if __name__ == '__main__':
    unittest.main()
