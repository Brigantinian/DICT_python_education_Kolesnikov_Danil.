import numpy as np

A = np.array([[1,2,3,4,5],[3,2,3,2,1],[8,0,9,9,1],[1,3,4,5,6]])
B = np.array([[1,1,4,4,5],[4,4,5,7,8],[1,2,3,9,8],[1,0,0,0,1]])
C = A + B
print(C)

while True:
    try:
      C = A + B
      break
    except:
        print("Error")




