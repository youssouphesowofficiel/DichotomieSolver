import matplotlib.pyplot as plt

def plot_convergence(history):
    """
    Affiche la convergence de l'algorithme en traçant l'évolution de a, b et c au fil des itérations.
    """
    iterations = [h[0] for h in history]
    a_values = [h[1] for h in history]
    b_values = [h[2] for h in history]
    c_values = [h[3] for h in history]

    plt.figure(figsize=(10, 6))
    plt.plot(iterations, a_values, label='Borne inférieure (a)')
    plt.plot(iterations, b_values, label='Borne supérieure (b)')
    plt.plot(iterations, c_values, label='Milieu (c)')
    plt.xlabel('Itérations')
    plt.ylabel('Valeur')
    plt.title('Convergence de la dichotomie')
    plt.legend()
    plt.grid(True)
    plt.show()
