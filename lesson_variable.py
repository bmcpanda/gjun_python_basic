string_chinese = "這是一個字串"
string_chinese = "這不是一個字串吧?"
number_1 = 5
number_2 = 10
print(string_chinese)
# 說明文 CTRL+? print(number_1 + number_2)

print(number_1, "+",number_2, "=", number_1 + number_2)
print(number_1, "-",number_2, "=", number_1 - number_2)
print(number_1, "*",number_2, "=", number_1 * number_2)
print(number_1, "/",number_2, "=", number_1 / number_2)
print(number_1, "//",number_2, "=", number_1 // number_2)
print(number_1, "%",number_2, "=", number_1 % number_2)

# 運算
import math
number_3 = -2.648
print(number_3, "的ABS絕對值", abs(number_3))
print(number_1, number_2, number_3, "的最大值", max(number_1,number_2,number_3))
print(number_1, number_2, number_3, "的最小值", min(number_1,number_2,number_3))
print(number_3, "的四捨五入是", round(number_3))
print(number_3, "的方根是", math.sqrt(abs(number_3)))
print(number_3, "的自然對數是", math.log(abs(number_3)))
print(number_3, "的二的對數是", math.log2(abs(number_3)))
print(number_3, "的5次方", pow(number_3, 5))
print(number_3, "的5次方", (number_3 ** 5))
print(number_3, "次方的自然數是", math.exp(number_3))
print(number_3, "次方的二是", math.exp2(number_3))

a = b = c = 50
c = 40
print(a, b, c)
c = a+b # c=100 a=150 b=250
a = c+b
b = a+c
print(a, b, c)
 
