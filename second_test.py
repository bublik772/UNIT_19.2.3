
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    # Сложение
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4

#  Умножение

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4


#  Деление

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 2) == 3

    
#  Вычитание

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4, 2) == 2