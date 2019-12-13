#!/usr/bin/env python3
from sys import exit
from numpy import arange

def check_num(num):
    snum = str(num)
    f1 = [False for _ in range(len(snum) - 1)]
    f2 = f1.copy()
    if len(snum) != 6:
        raise RuntimeError("Number must have 6 digits!")
    for i, d in enumerate(snum):
        if i == len(snum) - 1:
            break
        else:
            if snum[i] > snum[i + 1]:
                continue
            elif snum[i] == snum[i + 1]:
                f1[i] = True
                f2[i] = True
            else:
                f1[i] = True

    return (all(f1) and any(f2))

pwd_range = arange(136760, 595730 + 1)

## Test the stupid function
num = input("Enter a number of 6 digits: ")
ok = check_num(num)
print(f"{num} is {ok}")
exit(0)

# Loop over the input range
count = 0
for num in pwd_range:
    if check_num(num):
        count += 1

print(f"The nummber of valid pwd is {count}")
