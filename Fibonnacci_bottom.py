from datetime import datetime


# Fibonacci sequence, enter sequence number to caculate
def fib(n):
    if 0 < n == 1 or 0 < n == 2:
        return 1
    memo = [None] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


start = datetime.now()
if __name__ == '__main__':
    print('The result is: ' + str(fib(int(input('Enter Fibonnacci sequence number: ')))))
    print(datetime.now()-start)