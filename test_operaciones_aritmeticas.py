# test_operaciones_aritmeticas.py

import unittest
from operaciones_aritmeticas import OperacionesAritmeticas

class TestOperacionesAritmeticas(unittest.TestCase):
    def test_suma_dos_numeros_retorna_suma(self):
        # Arrange
        operando1 = 10
        operando2 = 15
        resultado_esperado = 25

        obj = OperacionesAritmeticas(operando1, operando2)

        # Act
        resultado_actual = obj.calcular_suma()

        # Assert
        self.assertEqual(resultado_esperado, resultado_actual, "Fallo la suma")

    def test_operador_no_numerico_lanza_excepcion(self):
        with self.assertRaises(TypeError):
            OperacionesAritmeticas(3, "a")

    def test_division_valida_retorna_resultado(self):
        # Arrange
        operando1 = 20
        operando2 = 4
        resultado_esperado = 5.0

        obj = OperacionesAritmeticas(operando1, operando2)

        # Act
        resultado_actual = obj.calcular_division()

        # Assert
        self.assertAlmostEqual(resultado_esperado, resultado_actual, 3,"Fallo la división")

    def test_division_por_cero_lanza_excepcion(self):
        with self.assertRaises(ZeroDivisionError):
            obj = OperacionesAritmeticas(10, 0)
            obj.calcular_division()

if __name__ == '__main__':
    unittest.main()
