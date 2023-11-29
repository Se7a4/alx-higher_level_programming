#!/usr/bin/python3
for alpha in range(97, 123, 1):
    if chr(alpha) == 'q' or chr(alpha) == 'e':
        continue
    print("{}".format(chr(alpha)), end="")
