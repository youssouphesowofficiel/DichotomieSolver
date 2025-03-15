from dichotomiesolver.solver import dichotomy_solver
from dichotomiesolver.utils import plot_convergence

def main():
    a = -8.9
    b = 9.9
    precision = 1e-6
    solution, history = dichotomy_solver(a, b, precision)
    print("Solution :", solution)
    # Afficher la convergence
    plot_convergence(history)

if __name__ == "__main__":
    main()
