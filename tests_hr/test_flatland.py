import pytest
from hacker_rank.flatland_space_stations import flatland_space_stations


def test_flatland_two_cities():
    # Caso de prueba 1
    n = 5
    c = [0, 4]
    assert flatland_space_stations(n, c) == 2


def test_flatland_three_cities():
    # Caso de prueba 2
    n = 20
    c = [0, 4, 15]
    assert flatland_space_stations(n, c) == 5


def test_flatland_n_cities():
    # Caso de prueba 3
    n = 6
    c = [0, 1, 2, 4, 3, 5]
    assert flatland_space_stations(n, c) == 0


def test_flatland_one_city():
    # Caso de prueba 4
    n = 100
    c = [50]
    assert flatland_space_stations(n, c) == 50


def test_flatland_minimal_case():
    # Caso de prueba 5
    n = 1
    c = [0]
    assert flatland_space_stations(n, c) == 0


def test_flatland_edge_cases():
    # Caso de prueba 6
    n = 100000
    c = [0, 99999]
    assert flatland_space_stations(n, c) == 49999


if __name__ == "__main__":
    pytest.main()
