# binary search that returns index of the target number in the sorted array.
# if not it should return -1.


def search(list, number):
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = int((left + right) / 2)
        if list[middle] == number:
            return middle
        elif number < list[middle]:
            right = middle
            print(str(right) + 'R')
        else:
            if number == list[right]:
                return right
            left = middle
            print(str(left) + 'L')
    return -1


# solve a shifted binary search

shifted_array1 = [-2, 3, 4, 7, 8, 9, 11, 13]
shifted_array2 = [13, -2, 3, 4, 7, 8, 9, 11]
shifted_array3 = [11, 13, -2, 3, 4, 7, 8, 9]
shifted_array4 = [9, 11, 13, -2, 3, 4, 7, 8]
shifted_array5 = [8, 9, 11, 13, -2, 3, 4, 7]
shifted_array6 = [7, 8, 9, 11, 13, -2, 3, 4]
shifted_array7 = [4, 7, 8, 9, 11, 13, -2, 3]
shifted_array8 = [3, 4, 7, 8, 9, 11, 13, -2]
array = [-2, 3, 4, 7, 8, 9, 11, 13]
target = -2


def new_shifted_search(list, number):
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2
        if list[middle] == number:
            return middle
        
        # Left part of the array
        if list[left] <= list[middle]:
            print('A')
            if number > list[middle] or number < list[left]:
                print('a')
                left = middle + 1
            else:
                print('b')
                right = middle - 1
        # Right part of the array
        else:
            print('B')
            if number < list[middle] or number > list[right]:
                print('a')
                right = middle - 1
            else:
                print('b')
                left = middle + 1
                print(left)
    return -1



def shifted_search(list, number):
    left = 0
    right = len(list) - 1

    while list[left] < list[right]:
        return search(list, number)

    while list[left] > list[right]:
        middle = (left + right) // 2
        if list[middle] == number:
            return middle
        elif list[middle] > list[right]:
            print('A')
            if number == list[left]:
                    return left
            left = middle + 1
            if list[left] < list[middle]:
                new_list = list[left :] + list [0 : left]
                print(new_list)
                return search(new_list, number) + left

        elif list[middle] < list[right]:
            print('B')
            if number == list[left]:
                    return left
            right = middle - 1
            if number == list[right]:
                    return right
            if list[right] > list[middle]:
                new_list = list[middle :] + list [: middle]
                print(new_list)
                print(right)
                return search(new_list, number) - right


if __name__ == '__main__':
    print(new_shifted_search(shifted_array5, target))