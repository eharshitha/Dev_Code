# imports
import math

# Variables


print("Enter a number")
n = int(input("\033[34m\033[1m>> "))
def calc_neg_pos(x):
    if x < 0:
        return "Negative!"
    elif x == 0:
        return "Zero!"
    else:
        return "Positive!"
def calc_odd_even(x):
    if x % 2 == 0:
        return "Even!"
    else:
        return "Odd!"
def calc_prime_comp(x):
    divisors = 0
    if x < 2:
        return "Undefined!"
    else:
        for i in range(2, x):
            if x % i == 0:
                divisors += 1
        if divisors > 0 :
            return "Composite!"
        else:
            return "Prime!"



print("\033[0m\033[1m===========Results===========")
print(f"\033[0mNegative or Positive: {calc_neg_pos(n)}")
print(f"Odd or Even: {calc_odd_even(n)}")
print(f"Prime or Composite: {calc_prime_comp(n)}")