# coding:utf-8
"""
基本的自动化测试脚本 basic_demo.py
"""
__author__ = 'zheng'

import unittest


class TestStringMethods(unittest.TestCase):

    def test_isupper(self):
        print 'end by test_isupper...'
        self.assertTrue('FOO'.isupper())

    def test_isupper1(self):
        print 'end by test_isupper1...'
        self.assertTrue('FOO'.isupper())


if __name__ == '__main__':
    unittest.main()

