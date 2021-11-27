import numpy as np

print("Sloshenie")
A = np.array([[1, 2, 3, 4, 5], [3, 2, 3, 2, 1], [8, 0, 9, 9, 1], [1, 3, 4, 5, 6]])
print(len(A))
B = np.array([[1, 1, 4, 4, 5], [4, 4, 5, 7, 8], [1, 2, 3, 9, 8], [1, 0, 0, 0, 1]])
print(len(B))
C = A + B
print(C)

while True:
    try:
        C = A + B
        break
    except:
        print("Error")
print("Umnoshenie")
D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Q = np.array(3)
T = D * Q
print(T)

