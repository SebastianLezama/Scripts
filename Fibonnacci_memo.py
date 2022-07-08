from datetime import datetime


# Fibonnacci sequence with memoization, enter sequence number to caculate
def fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    elif 0 < n == 1 or 0 < n == 2:
        result = 1
    elif n > 2:
        result = fib(n - 1, memo) + fib(n - 2, memo)
    else:
        print("No negative numbers please.")
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib(n, memo)


start = datetime.now()
if __name__ == '__main__':
    print('The result is: ' + str(fib_memo(int(input('Enter Fibonnacci sequence number: ')))))
    print(datetime.now()-start)


    # store a result