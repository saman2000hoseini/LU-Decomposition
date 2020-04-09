import numpy as np


def line_to_list():
    line = input()
    my_list = line.split()
    for i in range(0, len(my_list)):
        my_list[i] = float(my_list[i])
    return my_list


def print_mat(mat):
    print(mat)
    print("\n\n--------------------------------------------------------------------------------------\n\n")


def lu_decomposition():
    pivot_index = 0
    l = np.identity(n)
    for i in range(0, n):
        flag = True
        if A[i][pivot_index] == 0:
            flag = False
            for j in range(i + 1, n):
                if A[j][pivot_index] != 0:
                    A[[i, j]] = A[[j, i]]
                    flag = True
                    break
        if not flag:
            continue
        for j in range(i + 1, n):
            for k in range(0, n):
                A[j][k] = round(A[j][k], 2)
            if A[j][pivot_index] != 0:
                l[j][pivot_index] = A[j][pivot_index] / A[i][pivot_index]
                A[j] -= A[i] * A[j][pivot_index] / A[i][pivot_index]
        pivot_index += 1
        print_mat(A)
    return A, l


n = int(input())
A = []
for i in range(0, n):
    A.append(line_to_list())
A = np.array(A)
print_mat(A)
U, L = lu_decomposition()
print_mat(L)
