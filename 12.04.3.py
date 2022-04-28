# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
  #матрица
A = [...]
with open("matrix.txt", "w", encoding="utf-8") as file:
    for row in A:
        print(" ".join([str(x) for x in row]))
