from typing import List
import random


def random_list(n: int, m: int) -> List:
    result = []
    for i in range(n):
        result.append(random.randint(1, m))
    return result


if __name__ == '__main__':
    print(random_list(5, 10))
