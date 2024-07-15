def main() -> None:
    """Application initializer."""

    # arr: list[int] = [-8, -4, 0, 5, 10]
    arr: list[int] = [-8, -4, 0, 1, 0, 5, 10]
    print(is_monotonic(arr))


def is_monotonic(arr: list[int]) -> bool:
    """
    Determine if a list of integers is monotonic based on the detection of increasing or decreasing sequences, as consequense it's a contradiction to have both.

    Args:
        arr: list[int] -> List of integers

    Returns:
        bool -> True if the list is monotonic, False otherwise

    Example:
    >>> is_monotonic([-8, -4, 0, 5, 10])
    True
    >>> is_monotonic([-8, -4, 0, 5, 4, 10])
    False
    """

    if len(arr) < 3:
        return True
    temp: bool = arr[1] > arr[0]
    for i in range(len(arr) - 1):
        if arr[i + 1] == arr[i]:
            continue
        if (arr[i + 1] > arr[i]) != temp:
            return False
        temp = arr[i + 1] > arr[i]
    return True


if __name__ == '__main__':
    main()
