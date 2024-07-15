"""
Question 1: Rotate Array - Given an array, rotate the array to the right by k steps, where k is non-negative.
"""


def main() -> None:
    """Application initializer."""

    arr: list[int] = [-8, -4, 0, 5, 10]
    k: int = 2
    print(rotate_arr(arr, k))


def rotate_arr(arr: list[int], k: int) -> list[int]:
    """
    Given an array, rotate the array to the right by k steps, where k is non-negative.

    Args:
        arr: list[int] -> List of integers
        k: int -> Steps to rotate the array

    Returns:
        list[int] -> Rotated array

    Example:
    >>> rotate_arr([-8, -4, 0, 5, 10], 3)
    [0, 5, 10, -8, -4]
    >>> rotate_arr([-8, -4, 0, 5, 10], 1)
    [10, -8, -4, 0, 5]
    """

    if len(arr) < 2:
        return arr
    steps: int = abs(k) % len(arr)
    if steps == 0:
        return arr
    res = [-0 for _ in arr]
    for i, x in enumerate(arr):
        res[(i + steps) % len(arr)] = x
    return res


if __name__ == '__main__':
    main()
