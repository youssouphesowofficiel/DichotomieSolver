import argparse
from .solver import dichotomy_solver

def main():
    parser = argparse.ArgumentParser(description="Solveur numérique par dichotomie")
    parser.add_argument("--a", type=float, default=-8.9, help="Borne inférieure (défaut : -8.9)")
    parser.add_argument("--b", type=float, default=9.9, help="Borne supérieure (défaut : 9.9)")
    parser.add_argument("--precision", type=float, default=1e-6, help="Précision de l'arrêt (défaut : 1e-6)")
    args = parser.parse_args()

    try:
        solution, history = dichotomy_solver(args.a, args.b, args.precision)
        print("Solution trouvée :", solution)
    except ValueError as e:
        print("Erreur :", e)

if __name__ == "__main__":
    main()
