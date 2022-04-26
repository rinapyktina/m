# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    rows = 8
    col = 8
    array = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        assert len(row) == col
        array.append(row)

    kls = []

    for k in range(3):
        column = []
        for j in range(3):
            column.append(array[j][k])
        if column == array[k]:
            kls.append(k)
    print(kls)
