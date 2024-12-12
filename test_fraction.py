import unittest
from fraction import Fraction, ZeroDenominatorError, DivisionByZeroError, TypeError


class FractionTestCase(unittest.TestCase):
    """Test case for the Fraction class"""

    def test_init(self):
        """Test initialization of fractions"""
        # Test constructeur avec valeurs valides
        f = Fraction(1, 2)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        # Test constructeur avec valeurs par défaut
        f = Fraction()
        self.assertEqual(f.numerator, 0)
        self.assertEqual(f.denominator, 1)

        # Test simplification automatique
        f = Fraction(2, 4)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        # Test gestion du signe
        f = Fraction(-1, 2)
        self.assertEqual(f.numerator, -1)
        self.assertEqual(f.denominator, 2)
        f = Fraction(1, -2)
        self.assertEqual(f.numerator, -1)
        self.assertEqual(f.denominator, 2)

        # Test exceptions
        with self.assertRaises(ZeroDenominatorError):
            Fraction(1, 0)
        with self.assertRaises(TypeError):
            Fraction("1", 2)
        with self.assertRaises(TypeError):
            Fraction(1, "2")

    def test_str_representation(self):
        """Test string representation"""
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(-1, 2)), "-1/2")
        self.assertEqual(str(Fraction(4, 1)), "4")
        self.assertEqual(str(Fraction(0, 5)), "0")

    def test_mixed_number(self):
        """Test mixed number representation"""
        self.assertEqual(Fraction(5, 2).as_mixed_number(), "2 + 1/2")
        self.assertEqual(Fraction(3, 2).as_mixed_number(), "1 + 1/2")
        self.assertEqual(Fraction(-7, 2).as_mixed_number(), "-4 - 1/2")
        self.assertEqual(Fraction(2, 1).as_mixed_number(), "2")

    def test_mixed_number_edge_cases(self):
        f = Fraction(3, 3)
        self.assertEqual(f.as_mixed_number(), "1")

    def test_equality_edge_cases(self):
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            f == "1/2"

    def test_adjacent_to_with_integer(self):
        f = Fraction(1, 1)
        self.assertTrue(f.is_adjacent_to(2))

    def test_arithmetic_operations(self):
        """Test arithmetic operations"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)

        # Addition
        self.assertEqual(f1 + f2, Fraction(5, 6))
        self.assertEqual(f1 + 1, Fraction(3, 2))

        # Soustraction
        self.assertEqual(f1 - f2, Fraction(1, 6))
        self.assertEqual(f1 - 1, Fraction(-1, 2))

        # Multiplication
        self.assertEqual(f1 * f2, Fraction(1, 6))
        self.assertEqual(f1 * 2, Fraction(1, 1))

        # Division
        self.assertEqual(f1 / f2, Fraction(3, 2))
        self.assertEqual(f1 / 2, Fraction(1, 4))

        with self.assertRaises(DivisionByZeroError):
            f1 / Fraction(0, 1)

        # Puissance
        self.assertEqual(f1**2, Fraction(1, 4))
        self.assertEqual(f1**0, Fraction(1, 1))
        self.assertEqual(f1 ** (-2), Fraction(4, 1))

    def test_comparison(self):
        """Test comparison operations"""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        f3 = Fraction(1, 3)

        self.assertTrue(f1 == f2)  # Test fractions égales
        self.assertFalse(f1 == f3)  # Test fractions différentes
        self.assertFalse(f1 == 1)  # Test avec un entier

    def test_float_conversion(self):
        """Test conversion to float"""
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(-1, 2)), -0.5)
        self.assertEqual(float(Fraction(0, 1)), 0.0)

    def test_properties(self):
        """Test property checking methods"""
        # is_zero
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(1, 2).is_zero())

        # is_integer
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(1, 2).is_integer())

        # is_proper
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

        # is_unit
        self.assertTrue(Fraction(1, 2).is_unit())
        self.assertTrue(Fraction(-1, 3).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())

        # is_adjacent_to
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 2)  # Différence de 1 -> adjacent
        f3 = Fraction(5, 2)  # Différence de 2 -> non adjacent
        self.assertTrue(f1.is_adjacent_to(f2))
        self.assertFalse(f1.is_adjacent_to(f3))

    def test_abs(self):
        """Test absolute value of fractions"""
        self.assertEqual(abs(Fraction(-1, 2)), Fraction(1, 2))
        self.assertEqual(abs(Fraction(1, -2)), Fraction(1, 2))
        self.assertEqual(abs(Fraction(-3, -4)), Fraction(3, 4))

    def test_type_errors(self):
        """Test type checking and error handling"""
        f = Fraction(1, 2)

        with self.assertRaises(TypeError):
            f + "invalid"
        with self.assertRaises(TypeError):
            f - "invalid"
        with self.assertRaises(TypeError):
            f * "invalid"
        with self.assertRaises(TypeError):
            f / "invalid"
        with self.assertRaises(TypeError):
            f ** "invalid"
        with self.assertRaises(TypeError):
            f.is_adjacent_to("invalid")


if __name__ == "__main__":
    unittest.main()
