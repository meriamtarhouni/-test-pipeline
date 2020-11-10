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


def BenchMarkFacRecursive() :
    setup="from webserver import fact"     
    #The default number is 1000000
    print (timeit.timeit("fact(120)",setup=setup,number=10))
        

def BenchMarkFacIterative() :
    setup2="from webserver import fact_Iterative"
    print (timeit.timeit("fact_Iterative(120)",setup=setup2,number=10)) 


if __name__ == '__main__':
    BenchMarkFacRecursive()
    BenchMarkFacIterative()
    unittest.main()
    