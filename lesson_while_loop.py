# fibonacci num < 10000
F0 = 0
F1 = 1
#F2 = F0 + F1
list_fib = [F0, F1]

while list_fib[-1] < 10000:
    list_fib.append(list_fib[-2] + list_fib[-1])
print(list_fib,len(list_fib))
