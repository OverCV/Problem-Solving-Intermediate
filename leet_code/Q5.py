# Two Sum - You are given an array of Integers and another integer targetValue. Write a function that will take these inputs and return the indices of the 2 integers in the array that add up targetValue.


def main() -> None:
    """Application initializer."""

    # arr: list[int] = [1, 5, 6, 3, 4]
    # arr: list[int] = [10, 6, 5, 6, 5, 7]
    arr: list[int] = [3, 7, 5, 6, 8, 4]
    target: int = 4
    print(two_sum(arr, target))


def two_sum(arr: list[int], target: int):
    lprt: int = 0
    rptr: int = 0
    it: int = 0

    arr = sorted(arr)

    # El plan es ordenar el arreglo para tener los menores al objetivo puesto, es posible dos menores sumen al target pero no que al menos teniendo un mayor lo haga (sume el target)

    """
    00 01 02
    10 11 12
    20 21 22
    """

    leave = False
    while not leave:  #! Change!
        # (lprt <= tar) or (rptr <= tar)
        total = arr[lprt] + arr[rptr]
        if total == target:
            return lprt, rptr
        elif total > target:
            it += 1

        # leave = total > target
        # ...
