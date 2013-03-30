#coding:utf-8

import unittest

class testSample(unittest.TestCase):

    def test_sample(self):
        self.assertEqual((1+1), 2)

if __name__ == '__main__':
    unittest.main()

