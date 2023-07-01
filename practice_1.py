import numpy as np
n = 6
bubbles = np.random.choice(10, n, replace=False)
print(list(bubbles))
for round, _ in enumerate(bubbles):
    for index, _ in enumerate(bubbles):
        if index < n - round - 1:
            print(f"round:{round}, i:{bubbles[index]}, j:{bubbles[index + 1]}")            
            print(f"bubbles before:{bubbles}")
            if bubbles[index] > bubbles[index + 1]:
                temp = bubbles[index + 1]
                bubbles[index + 1] = bubbles[index]
                bubbles[index] = temp
            print(f"bubbles_after:{bubbles}")
print(enumerate(bubbles))
