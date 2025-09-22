"""Exercice 6.1 - Nombres premiers"""
from math import sqrt

#### Fonction secondaire
def isprime(valeur):
    """Teste si une valeur est un nombre premier."""
    premier = True
    if valeur<2 :
        premier = False
    else:
        for i in range (2, int(sqrt(valeur)+1)) :
            if valeur % i == 0 :
                premier = False
                break
    return premier


#### Fonction principale
def main():
    """Appelle la fonction secondaire.""" 
    # vos appels à la fonction secondaire ici
    val = int(input("Choose a number : "))
    if isprime(val) :
        print(val, " est un nombre premier ")
    else :
        print(val, " n'est pas un nombre premier ")
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
