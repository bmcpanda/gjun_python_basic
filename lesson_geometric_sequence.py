a0 = 1
r = 10

a1 = a0 * r
a2 = a1 * r
a3 = a2 * r
a4 = a3 * r
a5 = a4 * r
a6 = a5 * r
a7 = a6 * r
a8 = a7 * r
a9 = a8 * r
import time
start_time = time.time()
list_ar = [a0, a1, a2, a3, a4, a5, a6, a7, a8]
#1
print(sum(list_ar), time.time() - start_time)

#2
start_time = time.time()
sum_ar = a0 * (1 - pow(r, 9)) / (1 - r)
print(int(sum_ar), time.time() - start_time)

