import numpy as np

while True:
    menulist = """
        1.Add matrices
        2.Multiply matrix by a constant
        3.Multiply matrices
        0.Exit/Quit
        """
    print(menulist)

    action = int(input("SUKA BLYAT choose 0-3:"))

    if action == 0:
        print("Exit")
        break

    n1 = int(input("SUKA BLYAT enter n1:"))
    m1 = int(input("SUKA BLYAT enter please m1:"))
    n2 = int(input("SUKA BLYAT enter n2:"))
    m2 = int(input("SUKA BLYAT enter please m2:"))
    matrix1 = []
    matrix2 = []

    for i in range(n1):
        matrix1.append([])
        for k in range(m1):
            value = int(input(f"SUKA BLYAT [1 Matrix] enter {i + 1}:{k + 1}: "))
            matrix1[i].append(value)

    for i in range(n2):
        matrix2.append([])
        for k in range(m2):
            value = int(input(f"SUKA BLYAT [2 Matrix] enter {i + 1}:{k + 1}: "))
            matrix2[i].append(value)

    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    if action == 1:
        C = matrix1 + matrix2
        print(f"Matrix sum:\n {C}")
        print(f"[Matrix 1] length: {len(matrix1)}")
        print(f"[Matrix 2] length: {len(matrix2)}")

    elif action == 2:
        # Multiply matrix by a constan = int(input("Chto bi vi knkn"))
        # list = list.append (Multiply matrix by a constant)
        constant = int(input("PIDORAS please enter constant"))
        constantMatrix = np.array([constant])
        T = matrix1 * constant
        print(f"[Matrix 1] * constant:\n {T}")
        print(f"SWABRA [Matrix 1] length is {len(matrix1)}")
        print(f"KURWA constant length is {len(constantMatrix)}")
        continue

    elif action == 3:
        C = matrix1.dot(matrix2)
        print(f"Matrix multiply:\n {C}")
        print(f"[Matrix 1] length: {len(matrix1)}")
        print(f"[Matrix 2] length: {len(matrix2)}")
        continue

    else:
        print("Not valid")
        break
