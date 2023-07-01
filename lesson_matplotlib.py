from matplotlib import pyplot as plt
# 1
list_y = [1, 2, 3, 4, 6],[1, 4, 9, 16, 25]
# plt.plot(list_y)
# plt.show()
# plt.savefig("./plot_image/first_plot.jpg")
# plt.cla()
plt.xlabel("index")
plt.ylabel("value")
plt.legend(["first line"])
plt.title("first plot")

# 2
list_x_y = [(1,2), (2,4), (9,6), (7,10)]
# list_x_y.sort()
print(list_x_y)
plt.plot([x for x,y in list_x_y], [y for x,y in list_x_y], marker='.')
# plt.show()
plt.savefig("./plot_image/first_plot.jpg")
plt.cla()

# 3
n = range(1,30)
plt.plot(n, n, marker='o', linestyle='--', color="y")
plt.plot(n, [i*i for i in n] , "rs")
plt.plot(n, [i**3 for i in n] , "g^")
plt.legend(["n", "n**2", "n**3"])
plt.show()
plt.cla()

# 4
# plt.scatter()
n = range(1,30)
plt.scatter(n, n, c='y')
plt.scatter(n, [i*i for i in n], c='r')
plt.scatter(n, [i**3 for i in n], c='g')
plt.legend(["n","n*n","n*n*n"])
plt.savefig("./plot_image/forth_plot.jpg")
plt.cla()

# 5
import numpy as np
x = np.random.randint(1, 100, 1000)
y = np.random.randint(1, 100, 1000)
plt.scatter(x, y, c='y')
plt.savefig("./plot_image/fifth_plot.jpg")
plt.cla()

# 6
x = np.random.randint(1, 100, 10000)
plt.hist(x, bins= 99)
plt.savefig('./plot_image/sixth_histogram.jpg')
plt.cla()

# 7
x = [1, 2, 3, 4]
plt.pie(x, explode=[0,0,0,0.1], labels=['1', '2', '3', '4'])
plt.savefig('./plot_image/seventh_histogram.jpg')
plt.cla()
