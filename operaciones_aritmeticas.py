# operaciones_aritmeticas.py

class OperacionesAritmeticas:
    def __init__(self, operando1, operando2):
        if not isinstance(operando1, (int, float)) or not isinstance(operando2, (int, float)):
            raise TypeError("Ambos operandos deben ser numéricos (int o float).")
        self.operando1 = operando1
        self.operando2 = operando2

    def calcular_suma(self):
        return self.operando1 + self.operando2

    def calcular_division(self):
        if self.operando2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return self.operando1 / self.operando2
