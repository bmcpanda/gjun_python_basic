# N 個數字由小至大排序
# 共 N 輪
# 每一輪去比較手上的牌(已排好的部分)，比較大就排後面

import numpy as np



def insertion_sort(numbers):
    sorted_numbers = list() #排序好的部分
    for round in range(len(numbers)): #共N輪
        number = numbers[round]
        if round == 0:
            sorted_numbers.append(number)
        else:
            for index in range(len(sorted_numbers)-1, -1, -1): #去比較要放在哪裡
                if numbers[round] > sorted_numbers[index]: #如果比較大就放在後面
                    # sorted_numbers = sorted_numbers[:index] + numbers + sorted_numbers[index:] 錯誤
                    front = sorted_numbers[:index +1] # 0 ~ index
                    back = sorted_numbers[index + 1:] # index+1 ~ end
                    sorted_numbers = front + [number] + back
                    break
                if index == 0:
                    sorted_numbers = [number] + sorted_numbers
    return sorted_numbers

if __name__ == '__main__':
    N = 5
    numbers = np.random.choice(100, N,replace=False)
    print("Before: ", numbers)
    sorted_numbers = insertion_sort(numbers)
    print("After:", sorted_numbers)

