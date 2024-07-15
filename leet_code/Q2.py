def main() -> None:
    """Application initializer."""

    # arr: list[int] = [-8, -4, 0, 5, 10]
    arr: list[int] = [-8, -4, 0, 5, 10][::-1][::-1]
    print(is_monotonic(arr))


def is_monotonic(arr: list[int]) -> list[int]:
    """
    Monotonic Array:
    Question 2: An array is monotonic if it is either monotone increasing or monotone decreasing. An array is monotone increasing if all its elements from left to right are non-decreasing. An array is monotone decreasing if all  its elements from left to right are non-increasing. Given an integer array return true if the given array is monotonic, or false otherwise.
    """
    init = arr[0]
    last = arr[-1]

    if last >= init:
        print('INC')
        for x in arr:
            if x < init:
                return False
            init = x
    else:
        print('DEC')
        for x in arr:
            if x > init:
                return False
            init = x
    return True


if __name__ == '__main__':
    main()
