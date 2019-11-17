import unittest
import prueba
from getpass import getpass
import unittest
import os
import subprocess

class TestCommon(unittest.TestCase):
    pwd = getpass()

class test_Validar_Password(TestCommon):
    def test_a(self):
        self.assertEqual(self.pwd, 'duoc2019')
        print("Clave correcta")

    def test_Validar_Numero_Espacio(self):         
        s = 'duoc mundo asddas'
        self.assertEqual(s.split(), ['duoc', 'world']) 
        with self.assertRaises(TypeError): 
            s.split(2) 




        