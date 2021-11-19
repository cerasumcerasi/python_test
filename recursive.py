import sys


def recursive_call(num):
    return 1 if num == 0 else num * recursive_call(num - 1)


print(sys.getrecursionlimit())
print(recursive_call(10))

