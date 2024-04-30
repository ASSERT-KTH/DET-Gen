
import unittest
from temp_bug_qb import original_func as original_source
from temp_acc_qb import patched_func as patched_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['3 2 1\r\r', '6 5 4']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['0 0 0\r\r', '0 0 0']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['7 5 3\r\r', '2 4 6']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['2 8 1\r\r', '4 3 2']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['0 0 0\r\r', '1 1 1']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['5 3 2\r\r', '4 3 2']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['3 7 4\r\r', '1 5 2']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['3 3 3\r\r', '2 4 6']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['3 5 7\r\r', '4 2 6']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['10 15 20\r\r', '5 10 15']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    