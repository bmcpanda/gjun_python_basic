# a =   11 = 3
# b =  101 = 5
# s = 1000 = 8

# e = 12 => 18
# f = 2A => 42
# e = 3C => 60

a = "FFFFFF"
b = "ffffff"
# print(a + b)
# print(int(a), int(b), int(a)+int(b))
print(int(a, 16), int(b, 16), int(a, 16)+int(b, 16))

a = "1010"
b = "1011"
print(a + b)
print(int(a), int(b), int(a)+int(b))
print(int(a, 2), int(b, 2), int(a, 2)+int(b, 2))
c = int(a, 2) + int(b, 2)

binary_string = ""
while c > 1:
    remainder = c % 2
    c = c//2
    binary_string = str(remainder) + binary_string
    print(f"c={c}, r = {remainder}, bs ={binary_string}")

binary_string = str(c) + binary_string
print("binary string: ", binary_string)
