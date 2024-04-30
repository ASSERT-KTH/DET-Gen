
import unittest
from temp_bug_qb import original_func as original_source
from temp_acc_qb import patched_func as patched_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['10', '6 5 4 3 2 1 4 3 2 1']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['5\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['5', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['10\r', '100 90 80 70 60 50 40 30 20 10']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['5', '8 4 3 0 1 4 3 7 2 2 1 10 11']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['10', '3 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['12\r', '1 2 3 4 5 6 7 8 9 10 11 12 13']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['5\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['7', '12 11 10 9 8 7 6 5 4 3 2 1']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['10\r', '8 6 5 4 3 2 1']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    