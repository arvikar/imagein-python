from Core import docdata

__author__ = 'Pushkar'

import unittest


class MyTestCase(unittest.TestCase):
    def test_docdata(self):
        d = docdata.DocData(10,10, 10,20, 30,20, 30,10)
        self.assertAlmostEqual(d.d12,10,0)
        self.assertAlmostEqual(d.d23,20,0)
        self.assertAlmostEqual(d.d34,10,0)
        self.assertAlmostEqual(d.d14,20,0)
        self.assertAlmostEqual(d.angle1,45,0)
        self.assertAlmostEqual(d.angle2,63,0)
        self.assertAlmostEqual(d.angle3,34,0)
        self.assertAlmostEqual(d.angle4,18,0)

        self.assertAlmostEqual(d.zoom,1,0)
        self.assertAlmostEqual(d.alpha,0,0)
        self.assertAlmostEqual(d.beta,0,0)

        # same doc as above but with Alpha 60 and Beta 30
        d2 = docdata.DocData(10,10, 10,15, 27.321,15, 27.321,10 )
        d2.adaptToTemplate(d)
        self.assertAlmostEqual(d2.d12,5,0)
        self.assertAlmostEqual(d2.d23,17,0)
        self.assertAlmostEqual(d2.d34,5,0)
        self.assertAlmostEqual(d2.d14,17,0)
        self.assertAlmostEqual(d2.angle1,45,0)
        self.assertAlmostEqual(d2.angle2,56,0)
        self.assertAlmostEqual(d2.angle3,29,0)
        self.assertAlmostEqual(d2.angle4,20,0)

        self.assertAlmostEqual(d2.zoom,1,0)
        self.assertAlmostEqual(d2.alpha,60,0)
        self.assertAlmostEqual(d2.beta,30,0)

        self.assertAlmostEqual(d2.getPoint(20,15)[0],17.32,2)
        self.assertAlmostEqual(d2.getPoint(20,15)[1],7.5,2)

if __name__ == '__main__':
    unittest.main()
