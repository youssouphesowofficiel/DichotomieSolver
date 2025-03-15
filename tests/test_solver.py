import pytest
from dichotomiesolver.solver import f, dichotomy_solver

def test_f_returns_float():
    # Vérifie que f(x) retourne un float pour x dans l'intervalle
    x = 0
    result = f(x)
    assert isinstance(result, float)

def test_solver_solution_in_interval():
    # Vérifie que la solution se trouve bien dans l'intervalle donné
    solution, history = dichotomy_solver(-8.9, 9.9, precision=1e-6)
    assert -8.9 <= solution <= 9.9
    # Vérifie que f(solution) est suffisamment proche de zéro
    assert abs(f(solution)) < 1e-6

def test_solver_invalid_interval():
    # Vérifie qu'une erreur est levée si l'intervalle est invalide
    with pytest.raises(ValueError):
        dichotomy_solver(5, 5)
