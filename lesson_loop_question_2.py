#直角三角形

for i in range(5):
    print('*' * (i+1))

#等腰三角形
n = 6
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i+1))


#直角三角形
for i in range(n):
    print(" " * (n - i - 1) + "*" * (i + 1))