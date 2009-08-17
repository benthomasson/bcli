#!/usr/bin/env python

import unittest
from bcli import *

class Test(unittest.TestCase):

    def testLs(self):
        print 'ls'
        ls()

if __name__ == "__main__":
    unittest.main()

