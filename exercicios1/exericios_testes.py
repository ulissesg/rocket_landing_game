import unittest
from exercicios import *

class Test(unittest.TestCase):


    def test_maior(self):
        self.assertEqual(  maior(10,5)    ,  10 )  # VERIFICA SE CHAMADA DE maior(10,5) RESULTA EM 10
        self.assertEqual(  maior(5,10)    ,  10 )  # VERIFICA SE CHAMADA DE maior(5,10) RESULTA EM 10
        self.assertEqual(  maior(5,5)    ,  5 )
