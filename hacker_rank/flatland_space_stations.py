"""
Given n cities in a linear arrangement, some of which have space stations, determine the maximum distance from any city to its nearest space station. Cities are numbered from 0 to n-1, and each city is connected to the next by a road of length 1. The goal is to find the maximum of these minimum distances.
"""


def flatland_space_stations(n: int, c: list[int]):
    c.sort()
    return max(
        max([(c[i + 1] - c[i]) // 2 for i in range(len(c) - 1)]) if len(c) > 1 else 0,
        c[0],
        n - 1 - c[-1],
    )
