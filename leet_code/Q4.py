"""
Question 1: Rotate Array - Given an array, rotate the array to the right by k steps, where k is non-negative.
"""


def main() -> None:
    """Application initializer."""

    arr: list[int] = [1, 5, 6, 3, 4]
    print(max_container(arr))


def max_container(arr: list[int]) -> int:
    if len(arr) < 2:
        return min(arr)
    maximal = []
    for i, x in enumerate(arr):
        maximal.append(
            x
            * max(
                [abs(i - arr.index(y)) for y in arr if y >= x],
            )
        )
    print(f'{maximal}')
    return max(maximal)


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
