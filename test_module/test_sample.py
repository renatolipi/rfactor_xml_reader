#coding:utf-8

import unittest

from ..core.time_utils import prettify_laptime


#running tests: python -m rfactor_xml_reader.test_module.test_sample


class testUtils(unittest.TestCase):

    def test_sample(self):
        '''just an example on prettify_laptime'''
        pl_result = prettify_laptime(123)
        self.assertEqual(pl_result, '02\'3"0')


if __name__ == '__main__':
    unittest.main()

