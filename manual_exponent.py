from functools import reduce

import end as end

"""
manual_exponent(2, 3)
#> 8

manual_exponent(10, 2)
#> 100
"""

#Below is a iterative approach to the program

def manual_exponent(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))


