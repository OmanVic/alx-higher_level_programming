#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    j = 1
    con_str = ""
    new_str = str.split()
    for word in new_str:
        for letter in word:
            if i == n:
                i += 1
                continue
            else:
                con_str += letter
                i += 1
        if j != len(new_str):
            j += 1
            con_str += " "
    return con_str
