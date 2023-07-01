from collections import deque, namedtuple

deque_1 = deque([1, 2, 3])
deque_1.append(4)
deque_1.extend([5, 6, 7])
print(deque_1)
# 正常LIST要加東西到左邊
# list_a = ['a'] + ['b', 'c', 'd']
deque_1.appendleft(0)
deque_1.extendleft([10,9,8])
deque_1 = [11,12,13] + list(deque_1) #not deque anymore
print(deque_1)

deque_2 = deque(['a','b', 'c', 'd', 'e'], maxlen=7)
deque_2.rotate()
print(deque_2)
deque_2.rotate()
print(deque_2)
deque_2.rotate()
print(deque_2)
deque_2.rotate(3)
print(deque_2) #eabcd
deque_2.extendleft(['f', 'g', 'h', 'i']) #ihgfeab
print(deque_2)


#counter

from collections import Counter

counter = Counter([5, 5, 6, 7, 8, 9, 1, 3])
print(counter)
print(counter[5])

news = """
adshi   fahivfbisbid  fiulewhwlief hcfhvb  fehurhhogteru ewiu qpjecn disml
"""
words = news.lower().split()
word_frequency = Counter(words)
print(word_frequency)

#namedtuple
major_tuple = namedtuple("major_element_and_count", ["major_element", "count"])

m_1 = major_tuple(major_element= 9, count= 100)
m_2 = major_tuple(major_element= 15, count= 78)
print(m_1)
print(m_2)

print(m_1[0])
print(m_2[1])

print(m_1.major_element)