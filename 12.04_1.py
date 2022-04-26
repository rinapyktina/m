# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    n = int(input("n - "))
    m = int(input("m - "))
    A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        A.append(row)
    counter = 0
    for i in range(n):
        counterrow = 0
        for j in range(m):
            if A[i][j] < 0:
                counterrow += A[i][j]
        for j in range(m):
            if A[i][j] == 0:
                counter += counterrow
                break
    print(counter)
