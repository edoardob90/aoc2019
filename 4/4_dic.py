#!/usr/bin/env python3
import re
from sys import exit

def check_num(num):

    snum = str(num)

    if len(snum) != 6:
        raise RuntimeError("Number must have 6 digits!")

    for i in range(len(snum) - 1):
        if snum[i + 1] < snum[i]:
            return False
    return True

def check_doubles(num):

    snum = str(num)

    matches = re.findall('00+|22+|33+|44+|55+|66+|77+|88+|99+', snum)

    print(matches)

    # Check that we have matched something and that the longest match is only made by 2 identical digits, not more
    if matches and min([len(match) for match in matches]) == 2:
        return True
    else:
        return False

## Test the functions
#num = input("Enter a number of 6 digits: ")
#ok = check_num(num) and check_doubles(num)
#print(f"{num} is {ok}")
#exit(0)

# Loop over the input range
count = 0
for num in range(136760, 595730 + 1):
    if check_num(num) and check_doubles(num):
        count += 1

print(f"The nummber of valid pwd is {count}")
