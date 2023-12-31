# -*- coding: utf-8 -*-
"""Матрица.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18tM8WXDVHEhs_nDrFZzXMFdnW3xXrTUm
"""

import math

def mult2(A, B):
  result = []
  A_rows = len(A)
  A_cols = len(A[0])
  B_rows = len(B)
  if A_cols != B_rows:
    print('колличество столбцов первой матрицы не равно колличеству строк второй матрицы!')
    return

  result = [0 for col in range(A_rows)]
  for s in range(A_rows):
      for k in range(A_cols):
        result[s] += A[s][k] * B[k]
  return result

def sigma(x):
  return 1 / (1 + math.exp(-x))

def f_activate(A):
  res = []
  for x in A:
    res.append(sigma(x))
  return res

A = [[0.9, 0.3], [0.2, 0.8]]
B = [1.0, 0.5]

X = mult2(A, B)
X = f_activate(X)
print(X)