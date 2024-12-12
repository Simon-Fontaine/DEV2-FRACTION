# Exceptions personnalisées
class ZeroDenominatorError(Exception):
    """Exception levée quand le dénominateur est zéro"""

    pass


class DivisionByZeroError(Exception):
    """Exception levée lors d'une division par zéro"""

    pass


class TypeError(Exception):
    """Exception levée quand le type des arguments est incorrect"""

    pass


def gcd(a: int, b: int) -> int:
    """Calcule le PGCD de deux nombres
    PRE : a et b sont des entiers
    POST : Retourne le PGCD de a et b
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


class Fraction:
    """Class representing a fraction and operations on it

    Author: V. Van den Schrieck
    Date: October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """This builds a fraction based on some numerator and denominator.

        PRE:
            - num est un entier
            - den est un entier non nul
        POST:
            - Crée une fraction simplifiée avec numerator et denominator
        RAISES:
            - ZeroDenominatorError si den est 0
            - TypeError si num ou den ne sont pas des entiers
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Le numérateur et le dénominateur doivent être des entiers")
        if den == 0:
            raise ZeroDenominatorError("Le dénominateur ne peut pas être zéro")

        # Simplification et gestion du signe
        d = gcd(num, den)
        self._num = num // d if den > 0 else -num // d
        self._den = abs(den) // d

    @property
    def numerator(self) -> int:
        """Retourne le numérateur de la fraction
        PRE: -
        POST: Retourne le numérateur (int)
        """
        return self._num

    @property
    def denominator(self) -> int:
        """Retourne le dénominateur de la fraction
        PRE: -
        POST: Retourne le dénominateur (int)
        """
        return self._den

    def __str__(self) -> str:
        """Return a textual representation of the reduced form of the fraction
        PRE: -
        POST: Retourne une chaîne au format 'num/den' ou 'num' si den=1
        """
        if self._den == 1:
            return str(self._num)
        return f"{self._num}/{self._den}"

    def as_mixed_number(self) -> str:
        """Return a textual representation of the reduced form of the fraction as a mixed number
        PRE: -
        POST: Retourne une chaîne représentant le nombre mixte (ex: "5 + 2/3")
        """
        if abs(self._num) < self._den:
            return str(self)

        quotient = self._num // self._den
        remainder = abs(self._num % self._den)

        if remainder == 0:
            return str(quotient)

        if self._num < 0:
            return f"{quotient} - {remainder}/{self._den}"
        return f"{quotient} + {remainder}/{self._den}"

    def __add__(self, other):
        """Overloading of the + operator for fractions
        PRE: other est une Fraction ou un entier
        POST: Retourne une nouvelle Fraction résultant de l'addition
        RAISES: TypeError si other n'est pas une Fraction ou un entier
        """
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError(
                "L'opération n'est possible qu'entre fractions ou avec un entier"
            )

        num = self._num * other._den + other._num * self._den
        den = self._den * other._den
        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions
        PRE: other est une Fraction ou un entier
        POST: Retourne une nouvelle Fraction résultant de la soustraction
        RAISES: TypeError si other n'est pas une Fraction ou un entier
        """
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError(
                "L'opération n'est possible qu'entre fractions ou avec un entier"
            )

        num = self._num * other._den - other._num * self._den
        den = self._den * other._den
        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions
        PRE: other est une Fraction ou un entier
        POST: Retourne une nouvelle Fraction résultant de la multiplication
        RAISES: TypeError si other n'est pas une Fraction ou un entier
        """
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError(
                "L'opération n'est possible qu'entre fractions ou avec un entier"
            )

        return Fraction(self._num * other._num, self._den * other._den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions
        PRE: other est une Fraction non nulle ou un entier non nul
        POST: Retourne une nouvelle Fraction résultant de la division
        RAISES:
            - TypeError si other n'est pas une Fraction ou un entier
            - DivisionByZeroError si other est zéro
        """
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError(
                "L'opération n'est possible qu'entre fractions ou avec un entier"
            )
        if other.is_zero():
            raise DivisionByZeroError("Division par zéro impossible")

        return Fraction(self._num * other._den, self._den * other._num)

    def __pow__(self, power: int):
        """Overloading of the ** operator for fractions
        PRE: power est un entier
        POST: Retourne une nouvelle Fraction résultant de l'exponentiation
        RAISES: TypeError si power n'est pas un entier
        """
        if not isinstance(power, int):
            raise TypeError("L'exposant doit être un entier")

        if power < 0:
            return Fraction(self._den ** abs(power), self._num ** abs(power))
        return Fraction(self._num**power, self._den**power)

    def __eq__(self, other) -> bool:
        """Overloading of the == operator for fractions
        PRE: other est une Fraction ou un entier
        POST: Retourne True si les fractions sont égales, False sinon
        RAISES: TypeError si other n'est pas une Fraction ou un entier
        """
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError(
                "La comparaison n'est possible qu'entre fractions ou avec un entier"
            )

        return self._num * other._den == other._num * self._den

    def __float__(self) -> float:
        """Returns the decimal value of the fraction
        PRE: -
        POST: Retourne la valeur décimale de la fraction
        """
        return self._num / self._den

    def is_zero(self) -> bool:
        """Check if a fraction's value is 0
        PRE: -
        POST: Retourne True si la fraction vaut 0, False sinon
        """
        return self._num == 0

    def is_integer(self) -> bool:
        """Check if a fraction is integer
        PRE: -
        POST: Retourne True si la fraction est un entier, False sinon
        """
        return self._den == 1

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1
        PRE: -
        POST: Retourne True si |fraction| < 1, False sinon
        """
        return abs(self._num) < self._den

    def is_unit(self) -> bool:
        """Check if a fraction's numerator is 1 in its reduced form
        PRE: -
        POST: Retourne True si le numérateur est 1 ou -1, False sinon
        """
        return abs(self._num) == 1

    def __abs__(self):
        """Returns the absolute value of the fraction
        PRE : -
        POST : Retourne une nouvelle fraction représentant la valeur absolue de self
        """
        return Fraction(abs(self._num), self._den)

    def is_adjacent_to(self, other) -> bool:
        """Check if two fractions differ by a unit fraction
        PRE: other est une Fraction ou un entier
        POST: Retourne True si la différence est une fraction unitaire, False sinon
        RAISES: TypeError si other n'est pas une Fraction ou un entier
        """
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError(
                "La comparaison n'est possible qu'entre fractions ou avec un entier"
            )

        diff = abs(self - other)
        return diff.is_unit()
