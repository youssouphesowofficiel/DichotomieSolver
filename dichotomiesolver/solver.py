import math

def f(x):
    """
    Fonction définie pour la résolution par dichotomie.
    Lève une exception si x n'est pas dans l'intervalle (-9, 10).
    """
    if x >= 10 or x <= -9:
        raise ValueError("x must be in the interval (-9, 10) to avoid logarithm errors")
    return math.log(9.1) - 0.1 * math.log(10 - x) - 0.9 * math.log(9 + x)

def dichotomy_solver(a, b, precision=1e-6, max_iter=1000):
    """
    Résout l'équation f(x)=0 par la méthode de dichotomie.
    
    :param a: borne inférieure
    :param b: borne supérieure
    :param precision: précision désirée
    :param max_iter: nombre maximal d'itérations
    :return: solution approchée et historique des itérations sous forme de liste de tuples (itération, a, b, c, f(c))
    """
    history = []
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) et f(b) doivent avoir des signes opposés.")

    for i in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c)
        history.append((i, a, b, c, fc))
        if abs(b - a) < precision or fc == 0:
            return c, history
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2.0, history
