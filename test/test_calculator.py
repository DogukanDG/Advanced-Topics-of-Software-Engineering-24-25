from calculator import Calculator


class TestCalculator:
    def test_add(self):
        calc = Calculator()
        assert calc.add(1, 2) == 3

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(4, 2) == 2

    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(2, 5) == 10