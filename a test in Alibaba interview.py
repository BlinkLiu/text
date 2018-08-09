import numpy as np

N = int(input())
M = int(input())
N_col, N_row = input().strip().split(' ')
N_col, N_row = [int(N_col), int(N_row)]
matrix = []
for i in range(N_row):
    matr_N = list(map(int, input().strip().split(' ')))
    matrix.append(matr_N)
nn = 0
dic = {}
res = []

for nn in range(N_col):
    res_n = []
    for i in range(N_row):
        dic[i] = matrix[nn][i]
    visited = []
    for j in range(1, N_row):
        for jj in range(N_row):
            if jj != j:
                if dic[jj] != 0:
                    if jj in visited:
                        if dic[jj] > dic[j]+matrix[j][jj]:
                            dic[jj] = dic[j]+matrix[j][jj]
                    else:
                        dic[jj] = dic[j]+matrix[j][jj]
                        visited.append(jj)
                else:
                    dic[jj] = dic[j]+matrix[j][jj]
                    visited.append(jj)
    for j in range(M-2):
        visited = []
        dic_n = {}
        for i in dic.keys():
            for jj in range(N_row):
                if i != jj:
                    if jj in visited:
                        if dic_n[jj] > dic[i]+matrix[i][jj]:
                            dic_n[jj] = dic[i]+matrix[i][jj]
                    else:
                        dic_n[jj] = dic[i]+matrix[i][jj]
                        visited.append(jj)
        dic = dic_n
    for i in dic.keys():
        res_n.append(dic[i])
    res.append(res_n)
for i in range(N_col):
    print(" ".join(map(str, res[i])))
