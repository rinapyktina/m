# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    rows = int(input("number of rows: "))
    columns = int(input("number of columns: "))
    array = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        assert len(row) == columns
        array.append(row)

    array.sort(key = lambda row: sum(x for x in row if (x > 0 and x % 2 == 0)))
    print(array)