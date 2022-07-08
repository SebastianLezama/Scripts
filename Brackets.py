# queues problem: true if brackets are balanced

array = ("([])(){{}(())(){}}{")

shifted_array = [8, 9, 11, 13, -2, 3, 4, 7]

list = shifted_array[3:] + shifted_array[: 3]


# print(list)
# 
# print(len(list)-1)

# Find pivot point or smallest value

def firstN(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_first_n = sum(firstN(1000))
print(firstN(1000))
print(sum_of_first_n)

