def main() -> None:
    """Application initializer."""

    # arr: list[int] = [-8, -4, 0, 5, 10]
    arr: list[int] = [-8, -4, 0, 5, 10][::-1][::-1]
    print(arr)
    print(sorted_squared_array(arr))


def sorted_squared_array(arr: list[int]) -> list[int]:
    """
    Sorted Squared Array:
    Question 1: You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.
    """
    init: int = 0
    last: int = len(arr) - 1
    res: list[int] = []
    for _ in arr:
        if abs(arr[init]) > abs(arr[last]):
            res.insert(0, arr[init] ** 2)
            init += 1
        else:
            res.insert(0, arr[last] ** 2)
            last -= 1
    return res

    # non_dec = last >= init
    # for x in arr:
    #     if non_dec and x < init:
    #         return False
    #     elif x > init:
    #         return False


if __name__ == '__main__':
    main()
