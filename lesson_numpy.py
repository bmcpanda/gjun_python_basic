# pip import numpy
import numpy as np
x = np.random.randint(1, 100)
print(x)

n = np.random.randint(1, 50000)                                # n = 串列長度
major_element = np.random.randint(-1 * 10 ** 9, 10 ** 9)    # 隨機
part_2 = np.full(n - n // 2 + 1, major_element)             # major element 複製n/2個
part_1 = np.random.randint(-1 * 10 ** 9, 10 ** 9, n // 2 - 1) # 填滿剩下的n/2個
print(major_element)

test_case = np.concatenate([part_1, part_2])
np.random.shuffle(test_case)
print(len(test_case), n)