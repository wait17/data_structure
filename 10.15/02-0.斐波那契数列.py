import time
# 斐波那契数列


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n):
    if n == 1 or n == 2:   # n == 0 or n == 1 也可实现,哪种更好???
        return n
    return fib2(n - 1) + fib2(n - 2)


# start = time.time()
print(fib(5))
# end = time.time()
# dur = end - start
# print(dur)
