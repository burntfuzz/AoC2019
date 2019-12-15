#!/usr/bin/python3

import re

val1 = 152085
val2 = 670283

def check_never_decrease(passwd):
    return all(i <= j for i,j in zip(passwd, passwd[1:]))

def check_consecutive(passwd):
    return re.search(r"(\d)\1", passwd)

def check_strict_consecutive(passwd):
    consec = re.findall(r'((\d)\2+)', passwd)
    return any(len(x[0]) == 2 for x in consec)
        
def sum_possibilities(val1, val2):
    count = 0
    strict_count = 0
    for passwd_int in range(val1, val2+1):
        passwd = str(passwd_int)
        if check_consecutive(passwd) and check_never_decrease(passwd):
            count += 1
            if check_strict_consecutive(passwd):
                strict_count += 1
    return count, strict_count

count, strict_count = sum_possibilities(val1, val2)

print("Part 1: " + str(count))
print("Part 2: " + str(strict_count))