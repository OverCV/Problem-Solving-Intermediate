"""
Given n cities in a linear arrangement, some of which have space stations, determine the maximum distance from any city to its nearest space station. Cities are numbered from 0 to n-1, and each city is connected to the next by a road of length 1. The goal is to find the maximum of these minimum distances.
"""


def fair_rations(B: list[int]):
    if sum([b % 2 != 0 for b in B]) % 2 != 0:
        return 'NO'
    odds = [i for i, b in enumerate(B) if b % 2 != 0]
    print(odds)
    totals = [
        ((odds[(i * 2) + 1] - odds[i * 2] - 1) * 2) + 2
        for i in range(
            len(odds) // 2,
        )
    ]
    print(totals)
    return sum(totals)

    # 2*d + 2
    # Donde d es la distancia de iterar desde el elemento i hasta n
    # Puede que haya principio de invarianza si juntar los extremos cercanos a los medios cercanos:
    """
    abcd   -> 2,4=8
    a bc d -> 2,4,2,4=8

    a bc d -> 2,4,6,8=8
    ab cd  -> 2,2
    La mejor agrupación es la de entre elementos adyacentes
    """


# print(fair_rations([4, 5, 6, 7]))
# print(fair_rations([2, 3, 4, 5, 6]))
print(fair_rations([1, 2, 3, 5, 6, 7]))

"""
arr=[2, 3, 4, 5, 6]
    [   1     3]

"""
