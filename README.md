# DichotomieSolver
DichotomieSolver est un projet Python qui implémente la **méthode de dichotomie** pour trouver une solution approchée de l'équation \\( f(x) = 0 \\) avec une précision donnée.

Recherche de racine d'une fonction avec la méthode de dichotomie

Ce projet implémente la méthode de dichotomie pour trouver une solution approchée de l'équation  avec une précision donnée.

📌 Fonctionnalités

Utilisation de la méthode de bissection pour trouver une racine d'une fonction logarithmique.

Vérification préalable pour éviter les erreurs mathématiques liées aux logarithmes.

Gestion des erreurs et affichage de messages explicatifs en cas de problème.

🚀 Installation et exécution

1. Prérequis

Python 3.x installé sur votre machine.

2. Cloner le projet

git clone https://github.com/youssouphesowofficiel/DichotomieSolver
cd DichotomieSolver

3. Exécuter le script

python DichotomieSolver.py

📖 Explication du Code

Le programme suit les étapes suivantes :

Définition de la fonction 

Vérification de l'intervalle : s'assure que les logarithmes sont bien définis.

Vérification du changement de signe : la méthode de dichotomie nécessite .

Application de la méthode de dichotomie : réduit progressivement l'intervalle jusqu'à atteindre la précision voulue.

Affichage de la solution.

📌 Extrait du Code Principal

import math

def f(x):
    if x >= 10 or x <= -9:
        raise ValueError("x doit être dans l'intervalle (-9, 10) pour éviter les erreurs de log")
    return math.log(9.1) - 0.1 * math.log(10 - x) - 0.9 * math.log(9 + x)

a, b = -8.9, 9.9
precision = 1e-6

try:
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("L'intervalle choisi ne contient pas de racine")
    while (b - a) > precision:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            break
        elif fc * fa < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    print("La valeur de x est environ :", (a + b) / 2)
except ValueError as e:
    print("Erreur :", e)

🔍 Améliorations possibles

Permettre à l'utilisateur de saisir dynamiquement l'intervalle et la précision.

Ajouter un graphique pour visualiser la convergence de la méthode.

Étendre l'algorithme à d'autres méthodes de résolution comme Newton-Raphson.

📜 Licence

Ce projet est sous licence MIT - vous êtes libre de l'utiliser et de le modifier.

🎯 Auteur : [Youssouphe Sow]📅 Dernière mise à jour : 09 Mars 2025
