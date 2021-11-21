import decimal
import math


fruits = ["cocoa", "mango", "cherry"]
fruits_add = fruits.append("raspberry")
fruits[0] = "apple"

vegetables = ("carrot", "broccoli", "spinach")

vegetables += ("cauliflower",)


dec = 3.7 * 1.6
real = 5 * 7
my_dec = decimal.Decimal(5.9)
my_dict = {
    "brand": "Ford",
    "model": "Focus",
    "trim": "ST",
    "year": 2015
}

print(fruits)
print(vegetables)
print(f"{dec:.20f}")
print(real)
print(my_dec)
print(my_dict)
print(round(dec))
print(math.sqrt(dec))
print(my_dict["brand"])
print(vegetables[1])
print(fruits_add)
print(sorted(fruits))
print(vegetables)

