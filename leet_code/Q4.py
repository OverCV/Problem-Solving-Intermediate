"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
"""

from collections import Counter


def main() -> None:
    """Application initializer."""

    # arr: list[int] = [1, 5, 6, 3, 4]
    # arr: list[int] = [10, 6, 5, 6, 5, 7]
    arr: list[int] = [3, 7, 5, 6, 8, 4]
    print(max_container(arr))


def max_container(arr: list[int]) -> int:
    """
    Description: We first obtain all the elements that are higher than the current element. Then, we calculate the distance between the current element and the farthest element that is higher than the current element. Finally, we calculate the area of the container and store it in a list. The maximum value of the list is the maximum area of the container.

    Args:
        arr: list[int] -> List of integers

    Returns:
        int -> Maximum area of the container

    Example:
    >>> max_container([1, 5, 6, 3, 4])
    8
    >>> max_container([10, 6, 5, 6, 5, 7])
    25
    """

    if len(arr) == 0:
        return 0
    # maximal = []
    # for i, x in enumerate(arr):
    #     maximal.append(
    #         x
    #         * max(
    #             [abs(i - arr.index(y)) for y in arr if y >= x],
    #         )
    #     )
    # print(f'{maximal}')
    # return max(maximal)
    area: int = 0
    left: int = 0
    right: int = len(arr) - 1
    while left < right:
        height = min(arr[left], arr[right])
        max_area = height * (right - left)
        area = max(area, max_area)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return area


# def max_container(arr: list[int]) -> int:
#     # if len(arr) < 2:
#     #     return min(arr)

#     # ordered = sorted(arr, reverse=True)
#     # higher =  ordered[0]
#     # for x in ordered:
#     #     area =

#     # Iterar ordenadamente cada uno de los elementos y seleccionar el más lejano que tenga valor superior o igual a sí mismo.
#     maximal = 0
#     for i, x in enumerate(arr):
#         highers = [y for y in arr if y >= x]
#         dists = [
#             abs(
#                 i - arr.index(z),
#             )
#             for z in highers
#         ]
#         prod = x * max(dists)

#         # print([abs(i - arr.index(z)) for z in highers])
#         # farthest_idx = max(
#         #     [abs(i - highers.index(z)) for z in highers],
#         # )
#         print(f'({x}) {highers}->{dists} = {x}*{max(dists)}={prod}')

#         print()
#         # break


if __name__ == '__main__':
    main()
