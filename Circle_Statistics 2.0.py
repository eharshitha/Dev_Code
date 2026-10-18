import math

def sqr(n):
    return n * n

sep = " ~ "
pi = math.pi
r = float(input("Enter the radius of a circle: "))
print("\nResults:\n")
print(f"Radius = {r}")
print(f"Diameter = {r * 2}")
print(f"Circumference = {2 * r * pi}{sep}{round(2 * r * pi)}")
print(f"Area = {sqr(r) * pi}{sep}{round(sqr(r) * pi)}")
