nums = [2, 3, 4, 5, 6]

def tree_sum(nums):
    total = 0
    for i in nums:
        total += i
    return total

if __name__ == '__main__':
    print(tree_sum(nums))

new_list = [x for x in range(101, 301)] + [x for x in range(1, 101)]
new_list2 = [x for x in range(50) if x % 2 == 0]

print(new_list)
print(new_list2)
