from datetime import datetime


shifted_array1 = [13, -2, 3, 4, 7, 8, 9, 11]
shifted_array2 = [11, 13, -2, 3, 4, 7, 8, 9]
shifted_array3 = [9, 11, 13, -2, 3, 4, 7, 8]
shifted_array4 = [8, 9, 11, 13, -2, 3, 4, 7]
shifted_array5 = [7, 8, 9, 11, 13, -2, 3, 4]
shifted_array6 = [4, 7, 8, 9, 11, 13, -2, 3]
shifted_array7 = [3, 4, 7, 8, 9, 11, 13, -2]
shifted_array8 = [x for x in range(10001, 30000001)] + [x for x in range(1, 10001)]


def find_pivot(list):
    left = 0
    right = len(list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if list[mid] <= list[mid - 1]:
            return mid
        if list[mid] > list[mid + 1]:
            return mid + 1

        # Left side of the array
        if list[right] < list[mid]:
                # print('A')
                left = mid + 1

        else:
        # Right side of the array
            if list[left] > list[mid]:
                # print('B')
                right = mid - 1
    return 'Fail'


start = datetime.now()
if __name__ == '__main__':
    print(shifted_array8[find_pivot(shifted_array8)])
    print(datetime.now() - start)
    
