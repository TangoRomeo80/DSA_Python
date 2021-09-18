# the following lines are reserved for imports
#
#

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# driver code
if __name__ == '__main__':
    print(factorial(5))
