from collections import Counter #class
import numpy
# list_nums = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,8,7,9,9,9,9,9,9,9,9,9,9,99,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,99,9]

# pip import numpy
import numpy as np
n = np.random.randint(1, 50000)                                # n = 串列長度
major_element = np.random.randint(-1 * 10 ** 9, 10 ** 9)    # 隨機
part_2 = np.full(n - n // 2 + 1, major_element)             # major element 複製n/2個
part_1 = np.random.randint(-1 * 10 ** 9, 10 ** 9, n // 2 - 1) # 填滿剩下的n/2個
print(major_element)

test_case = np.concatenate([part_1, part_2])
np.random.shuffle(test_case)
print(len(test_case), n)

list_nums = test_case
number_counter = Counter(list_nums) # instance 實體
print(number_counter, len(list_nums))
#print("most_common(1): ", number_counter.most_common(1))
#print("most_common(1)[0]: ", number_counter.most_common(1)[0])
print("most_common(1)[0][0]: ", number_counter.most_common(1)[0][0])
#print(number_counter.most_common())