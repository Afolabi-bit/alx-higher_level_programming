#!/usr/bin/python3
i = 122
while (i >= 65):
    if (i > 90) and (i < 97):
        break
    print("{}".format(chr(i)), end="")
    if i < 97:
        i += 31
        continue
    i -= 33
