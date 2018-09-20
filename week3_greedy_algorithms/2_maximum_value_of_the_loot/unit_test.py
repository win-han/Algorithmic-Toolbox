# test _Rat ional . py
# unittest example
import sys
import unittest

sys.path.insert(O, '..')
from Rational import *


class RationalTest(unittest.TestCase):

    def testConstructorOnelnt(self):
        r = Rational(-3)
        self.assertEqual(str(r), '-3/1')

    def testConstructorTwolnt(self):
        r = Rational(3, 4)
        self.assertEqual(str(r), '3/4')

    def testMul(self):
        r1 = Rational(2, 3)
        r2 = Rational(3, 4)
        r3 = r1 * r2
        self.assertEqual(str(r3), '6/12')


def main(argv):
    unittest.main()


if __name__ == '__ main __':
    main(sys.argv)