#!/usr/bin/python3
for x in range(0, 8):
    for y in range(0, 10):
        if x != y and y > x:
            print(f"{x}{y}", end=", ")
print("89")
