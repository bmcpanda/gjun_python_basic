import math
import numpy as np
n = 3
numbers = np.random.choice(1000, n, replace=False)

print(numbers, math.gcd(*numbers))

# minimum numbers of numbers
# divisor of min number
# check if divisor is common divisor
# max common divisor

def find_divisor_of_min(list_of_numbers):
    #1
    min_number = min(list_of_numbers)
    #2
    divisors_of_min = list()
    for n in range(1, min_number + 1):
        if min_number % n == 0:
            divisors_of_min.append(n)
    print(min_number, divisors_of_min)
    return divisors_of_min

divisors = find_divisor_of_min(numbers)
#3
def find_great_common_divisors(list_of_numbers):
    divisors = find_divisor_of_min(list_of_numbers)
    list_of_common_divisors = list()
    for divisor in divisors:
        is_common_divisor = True
        for number in list_of_common_divisors:
            if number % divisor == 0:
                continue
            else:
                is_common_divisor = False
                break
        if is_common_divisor == True:
            list_of_common_divisors.append(divisor)
    print(list_of_common_divisors)

    return max(list_of_common_divisors)

if __name__ == '__main__':
    n = 2
    for _ in range(3):
        numbers = np.random.choice(1000, n, replace=False)
        print("numbers: ", numbers, math.gcd(*numbers))
        result = find_great_common_divisors(numbers)
        print(result)
                                   
