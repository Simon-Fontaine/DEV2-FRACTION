from fraction import Fraction, ZeroDenominatorError, DivisionByZeroError, TypeError


def demo_fraction():
    print("=== Démonstration de la classe Fraction ===\n")

    # 1. Création et affichage de fractions
    print("1. Création et affichage de fractions")
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)  # Sera simplifié en 1/2
    f3 = Fraction(-3, 6)  # Sera simplifié en -1/2

    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    print(f"f3 = {f3}")

    # 2. Nombres mixtes
    print("\n2. Représentation en nombres mixtes")
    f4 = Fraction(5, 2)
    print(f"{f4} en nombre mixte : {f4.as_mixed_number()}")

    # 3. Opérations arithmétiques
    print("\n3. Opérations arithmétiques")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 - f2 = {f1 - f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
    print(f"f1 ** 2 = {f1 ** 2}")

    # 4. Comparaisons
    print("\n4. Comparaisons")
    print(f"f1 == f2: {f1 == f2}")
    print(f"f1 == f3: {f1 == f3}")

    # 5. Propriétés
    print("\n5. Vérification des propriétés")
    print(f"{f1} est un entier ? {f1.is_integer()}")
    print(f"{f1} est une fraction propre ? {f1.is_proper()}")
    print(f"{f1} est une fraction unitaire ? {f1.is_unit()}")

    # 6. Fractions adjacentes
    print("\n6. Fractions adjacentes")
    f5 = Fraction(3, 2)
    print(f"{f1} et {f5} sont adjacentes ? {f1.is_adjacent_to(f5)}")

    # 7. Gestion des erreurs
    print("\n7. Démonstration de la gestion des erreurs")
    try:
        f_error = Fraction(1, 0)
    except ZeroDenominatorError as e:
        print(f"Erreur attendue : {e}")

    try:
        result = f1 / Fraction(0, 1)
    except DivisionByZeroError as e:
        print(f"Erreur attendue : {e}")


if __name__ == "__main__":
    demo_fraction()
