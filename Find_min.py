from datetime import datetime


shifted_array1 = [13, -2, 3, 4, 7, 8, 9, 11]
shifted_array2 = [11, 13, -2, 3, 4, 7, 8, 9]
shifted_array3 = [9, 11, 13, -2, 3, 4, 7, 8]
shifted_array4 = [8, 9, 11, 13, -2, 3, 4, 7]
shifted_array5 = [7, 8, 9, 11, 13, -2, 3, 4]
shifted_array6 = [4, 7, 8, 9, 11, 13, -2, 3]
shifted_array7 = [3, 4, 7, 8, 9, 11, 13, -2]
shifted_array8 = [x for x in range(10001, 30000001)] + [x for x in range(1, 10001)]



def find_min(nums) -> int:
    result = nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] < nums[right]:
            result = min(result, nums[left])
            break

        mid = (left + right) // 2
        result = min(result, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1
    return result

start = datetime.now()
if __name__ == '__main__':
    print(find_min(shifted_array8))
    print(datetime.now() - start)
