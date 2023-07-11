import numpy as np
n = 6
bubbles = np.random.choice(100, n, replace=False)
print(list(bubbles))

# n=6
# r1:idx5 r2:idx4 r3:idx3 r4:idx2 ==> r + idx = 6, idx = 6 - r
# Time Complexity = O(n**2)

for round, _ in enumerate(bubbles):
    for index, _ in enumerate(bubbles):
        if index > 0 and index < n - round:
            print(f"round:{round}, i:{bubbles[index - 1]}, j:{bubbles[index]}")
            print(f"bubbles before: {bubbles}")
            if bubbles[index - 1] > bubbles[index]:
                temp = bubbles[index - 1]
                bubbles[index - 1] = bubbles[index]
                bubbles[index] = temp
            print(f"bubbles_after : {bubbles}")

print(sorted(bubbles))

# index - 1 edit index
