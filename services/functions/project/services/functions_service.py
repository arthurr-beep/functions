def fibonacci(number: int) -> int:
    """[Compute the fibonacci series of a positive integer]

    Args:
        number (int): [input non-negative integer]

    Returns:
        int: [function result]
    """

    if number <= 1:
        return number

    if number == 2:
        return 1

    current = 0
    previous = 1
    before_previous = 1

    # Add 1 since the range ftn excludes the upper limit
    for idx in range(3, number + 1):
        current = previous + before_previous
        before_previous = previous
        previous = current

    return current


def factorial(number: int) -> int:
    """Computes The factorial of a given positive integer

    Args:
        number (int): [input integer]

    Returns:
        int: [result of computation]
    """

    fact = 1

    for idx in range(2, number + 1):
        fact *= idx

    return fact


class Ackerman:
    def __init__(self) -> None:
        self.memory = {}

    def compute(self, number_1: int, number_2: int) -> int:

        if number_1 in self.memory and number_2 in self.memory[number_1]:
            return self.memory[number_1][number_2]

        else:
            result = 0

            if number_1 == 0:
                result = number_2 + 1
            if number_1 == 1:
                result = number_2 + 2
            elif number_2 == 0:
                result = self.compute(number_1 - 1, 1)

            else:
                result = self.compute(
                    number_1 - 1, self.compute(number_1, number_2 - 1)
                )

            if number_1 not in self.memory:
                self.memory[number_1] = {}

            self.memory[number_1][number_2] = result
        return result
