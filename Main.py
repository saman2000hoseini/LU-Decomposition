import numpy as np


def fix_round(x, acc):
    if x == 0 or x == -0:
        return 0
    return round(x, 3)


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
        if U[i][pivot_index] == 0:
            flag = False
            for j in range(i + 1, n):
                if U[j][pivot_index] != 0:
                    U[[i, j]] = U[[j, i]]
                    flag = True
                    break
        if not flag:
            continue
        for j in range(i + 1, n):
            for k in range(0, n):
                U[j][k] = fix_round(U[j][k], 2)
            if U[j][pivot_index] != 0:
                l[j][pivot_index] = U[j][pivot_index] / U[i][pivot_index]
                l[j][pivot_index] = fix_round(l[j][pivot_index], 2)
                U[j] -= U[i] * U[j][pivot_index] / U[i][pivot_index]
        pivot_index += 1
        print_mat(U)
    return l


def forward_substitution(b):
    lb = np.hstack((L, b))
    pivot_index = 0
    for i in range(0, n):
        flag = True
        if lb[i][pivot_index] == 0:
            flag = False
            for j in range(i + 1, n):
                if lb[j][pivot_index] != 0:
                    lb[[i, j]] = lb[[j, i]]
                    flag = True
                    break
        if not flag:
            continue
        for j in range(i + 1, n):
            if lb[j][pivot_index] != 0:
                lb[j] -= lb[i] * lb[j][pivot_index] / lb[i][pivot_index]
            for k in range(0, 2 * n):
                lb[j][k] = fix_round(lb[j][k], 2)
        lb[i] /= lb[i][pivot_index]
        for k in range(0, 2 * n):
            lb[i][k] = fix_round(lb[i][k], 2)
        pivot_index += 1
        print_mat(lb)
    return lb[:, n:]


def backward_substitution(y):
    uy = np.hstack((U, y))
    pivot_index = n - 1
    for i in range(n - 1, -1, -1):
        flag = True
        if uy[i][pivot_index] == 0:
            flag = False
            for j in range(i - 1, -1, -1):
                if uy[j][pivot_index] != 0:
                    uy[[i, j]] = uy[[j, i]]
                    flag = True
                    break
        if not flag:
            continue
        for j in range(i - 1, -1, -1):
            if uy[j][pivot_index] != 0:
                uy[j] -= uy[i] * uy[j][pivot_index] / uy[i][pivot_index]
            for k in range(0, 2 * n):
                uy[j][k] = fix_round(uy[j][k], 2)
        uy[i] /= uy[i][pivot_index]
        for k in range(0, 2 * n):
            uy[i][k] = fix_round(uy[i][k], 2)
        pivot_index -= 1
        print_mat(uy)
    return uy[:, n:]


n = int(input())
U = []
for i in range(0, n):
    U.append(line_to_list())
U = np.array(U)
print_mat(U)
L = lu_decomposition()
print_mat(L)
L_Inverse = forward_substitution(np.identity(n))
U_Inverse = backward_substitution(np.identity(n))
print_mat(U_Inverse)
print_mat(L_Inverse)
A_Inverse = np.multiply(U_Inverse, L_Inverse)
print_mat(A_Inverse)
