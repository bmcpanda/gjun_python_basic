list_a = range(1, 101)
print(list(list_a))
list_square = list()
for x in list_a:
    list_square.append(x**2)
print(list_square)

#comprehension
list_square = [number ** 2 for number in list_a]
print(list_square)

#square sum
list_square_sum = list()
# for number in list_square:
#     list_square_sum.append(sum(number))
# print(list_square_sum)
#Q2
c = 0
for x in list_a:
    c = c + x ** 2
    list_square_sum.append(c)
print(list_square_sum)

#Q_3 handle square odd only
list_square_odd = list()
for x in list_a:
    if x % 2 == 0:
        list_square_odd.append(x)
        continue
    else :
        list_square_odd.append(x**2)
        print("square it!!!!", x)
#list_square = [ x**2 for x in list_a if x % 2 == 1 else x]
#print(list_square_odd, len(list_square_odd))

#Q_4:
# square: 1-50:\
list_square_50 = list()
for x in list_a:
    if x > 50:
        print ("over 50")
        break
    list_square_50.append(x**2)
print(list_square_50, len(list_square_50))

#Q_4 while
list_square_50 = list()
index = 0
while index < len(list_a):
    if list_a[index] > 50:
        break
    list_square_50.append(x**2)
print(list_square_50, len(list_square_50))

############################################## to loop question






