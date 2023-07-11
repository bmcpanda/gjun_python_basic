import numpy as np


def merge(left_array, right_array):
    result = list()
    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] < right_array[0]:
            result.append(left_array.pop(0))
        else:
            result.append(right_array.pop(0))

    if len(left_array) > 0:
        result += left_array
    else:
        result += right_array

    return (result)


def merge_sort(array):
    if len(array) == 1: #剩一個，直接排好
        return array
    # 切一半
    middle_index = len(array)//2
    left_array, right_array = array[:middle_index], array[middle_index:]
    #排好兩半
    sorted_left_array = merge_sort(left_array)
    sorted_right_array = merge_sort(right_array)
    #合併
    sorted_array = merge(sorted_left_array, sorted_right_array)
    return sorted_array


if __name__ == '__main__':
    # left_array = sorted(np.random.choice(100, 5, replace=False))
    # right_array = sorted(np.random.choice(100, 5, replace=False))
    # print(left_array)
    # print(right_array)
    # print(merge(left_array, right_array))

    # Numpy Pop = np.delete
    numbers = np.random.choice(100, 10, replace=False).tolist()
    print(numbers)
    print(merge_sort(numbers))
