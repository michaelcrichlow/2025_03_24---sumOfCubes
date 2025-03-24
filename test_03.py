def is_perfect_cube(n: int) -> bool:
    idx = 1
    num = idx * idx * idx
    while True:
        if num == n:
            return True
        elif num < n:
            idx += 1
            num = idx * idx * idx
        elif num > n:
            return False
        
# NOTE: could also just check if the cbrt() of a number is an
# integer, but that seems to get inconsistent results from various
# versions of Python
# e.g.:
#    if math.cbrt(val).is_integer():
#        total += val
#
# The above example works with Python 3.11 but not 3.13
# So, I wrote the is_perfect_cube() function to have a solution
# that works on all versions of Python (within reason LOL).

import math

def sumOfCubes(l: list[int]) -> int:
    total = 0
    for val in l:
        if is_perfect_cube(val):
            total += val
    return total

def main() -> None:
    print(sumOfCubes([1, 8, 27, 4, 5]))  # 36


if __name__ == '__main__':
    main()
