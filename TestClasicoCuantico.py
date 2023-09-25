import unittest
import ClasicoCuantico as cc
import numpy as np
import math

class TestLibClasicoCuantico(unittest.TestCase):
    m1 = np.array([[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 1]])
    v1 = [2, 3, 0, 2, 4, 1]

    def test_simula_Canicas(self):
        prueba_1 = cc.simulaCanicas(self.m1,self.v1,1)
        self.assertAlmostEqual(prueba_1[0], 2)
        self.assertAlmostEqual(prueba_1[1], 0)
        self.assertAlmostEqual(prueba_1[2], 7)
        self.assertAlmostEqual(prueba_1[3], 0)
        self.assertAlmostEqual(prueba_1[4], 2)
        self.assertAlmostEqual(prueba_1[5], 1)

        prueba_2 = cc.simulaCanicas(self.m1, self.v1, 2)
        self.assertAlmostEqual(prueba_2[0], 2)
        self.assertAlmostEqual(prueba_2[1], 0)
        self.assertAlmostEqual(prueba_2[2], 2)
        self.assertAlmostEqual(prueba_2[3], 0)
        self.assertAlmostEqual(prueba_2[4], 0)
        self.assertAlmostEqual(prueba_2[5], 8)

        prueba_3 = cc.simulaCanicas(self.m1, self.v1, 0)
        self.assertAlmostEqual(prueba_3[0], 2)
        self.assertAlmostEqual(prueba_3[1], 3)
        self.assertAlmostEqual(prueba_3[2], 0)
        self.assertAlmostEqual(prueba_3[3], 2)
        self.assertAlmostEqual(prueba_3[4], 4)
        self.assertAlmostEqual(prueba_3[5], 1)

    m2 = np.array([[0, 0, 0, 0, 0, 0, 0, 0],[1/3, 0, 0, 0, 0, 0, 0, 0], [1/3, 0, 0, 0, 0, 0, 0, 0], [1/3, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1/2, 0, 0, 1, 0, 0, 0], [0, 1/2, 1/2, 0, 0, 1, 0, 0], [0, 0, 1/2, 1/2, 0, 0, 1, 0], [0, 0, 0, 1/2, 0, 0, 0, 1]])
    def test_simul_multi_slit(self):
        prueba_1 = cc.simul_multi_slit(self.m2,1,True)
        self.assertAlmostEqual(prueba_1[0], 0)
        self.assertAlmostEqual(prueba_1[1], 1/3)
        self.assertAlmostEqual(prueba_1[2], 1/3)
        self.assertAlmostEqual(prueba_1[3], 1/3)
        self.assertAlmostEqual(prueba_1[4], 0)
        self.assertAlmostEqual(prueba_1[5], 0)
        self.assertAlmostEqual(prueba_1[6], 0)
        self.assertAlmostEqual(prueba_1[7], 0)

        prueba_1 = cc.simul_multi_slit(self.m2, 2, True)
        self.assertAlmostEqual(prueba_1[0], 0)
        self.assertAlmostEqual(prueba_1[1], 0)
        self.assertAlmostEqual(prueba_1[2], 0)
        self.assertAlmostEqual(prueba_1[3], 0)
        self.assertAlmostEqual(prueba_1[4], 1/6)
        self.assertAlmostEqual(prueba_1[5], 1/3)
        self.assertAlmostEqual(prueba_1[6], 1/3)
        self.assertAlmostEqual(prueba_1[7], 1/6)

    m3 = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                   [1/2, 0, 0, 0, 0, 0, 0, 0],
                   [1/2, 0, 0, 0, 0, 0, 0, 0],
                   [0,((complex(-1,1))/math.sqrt(6)), 0, 0, 0, 0, 0, 0],
                   [0, ((complex(-1,-1))/math.sqrt(6)), 0, 0, 1, 0, 0, 0],
                   [0, ((complex(1,-1))/math.sqrt(6)), ((complex(-1,1))/math.sqrt(6)), 0, 0, 1, 0, 0],
                   [0, 0, 0, ((complex(-1,-1))/math.sqrt(6)), 0, 0, 1, 0],
                   [0, 0, 0, ((complex(1,-1))/math.sqrt(6)), 0, 0, 0, 1]])

    def test_simul_multi_slit_imag(self):
        prueba_1 = cc.simul_multi_slit_imag(self.m3,1,True)
        self.assertAlmostEqual(prueba_1[0], complex(0,0))
        self.assertAlmostEqual(prueba_1[1], complex(1/2,0))
        self.assertAlmostEqual(prueba_1[2], complex(1/2,0))
        self.assertAlmostEqual(prueba_1[3], complex(0,0))
        self.assertAlmostEqual(prueba_1[4], complex(0,0))
        self.assertAlmostEqual(prueba_1[5], complex(0,0))
        self.assertAlmostEqual(prueba_1[6], complex(0,0))
        self.assertAlmostEqual(prueba_1[7], complex(0,0))


if __name__ == '__main__':
    unittest.main()