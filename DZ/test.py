import fib
import unittest
import time



def test_zero():
    assert (list(fib.Get_Fib_n(0)) == [])

def test_one():
    assert (list(fib.Get_Fib_n(1)) == [1])

def test_three():
    assert (list(fib.Get_Fib_n(3)) == [1, 1, 2])



#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestFib(unittest.TestCase):
  #Each test method starts with the keyword test_
    def test_zero(self):
        self.assertEqual(list(fib.Get_Fib_n(0)), [])

    def test_one(self):
        self.assertEqual(list(fib.Get_Fib_n(1)), [1])

    def test_three(self):
        self.assertEqual(list(fib.Get_Fib_n(3)), [1, 1, 2])

    def test_time(self):
        begin = time.time()
        a = fib.Get_Fib_n(200000)
        end = time.time()
        self.assertLess(end - begin, 1)

if __name__ == '__main__':
    unittest.main()