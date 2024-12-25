"""
# Get Distinct Numbers (Assignment)

## Problem Statement

Implement a function `getDistinctNumbers` that takes a list of numbers as input and returns a list containing only the distinct numbers from the input list.

## Instructions

-   Implement the `getDistinctNumbers` function inside the `distinctNumbers.py` file.
-   It should take a single argument `numbers`, which is a list of numbers.
-   The function should return a new list containing only the distinct numbers from the input list.
-   The order of elements should be same as the order in which they occur in the input list
"""
def getDistinctNumbers(numbers):
    return list(dict.fromkeys(numbers))

if __name__ == '__main__':
        numbers = [1, 2, 3, 4, 4, 5, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]
        print(getDistinctNumbers(numbers))
        assert getDistinctNumbers(numbers) == expected_result