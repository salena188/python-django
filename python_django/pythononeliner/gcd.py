print("\t------GCD ----")
a = 12
b = 18

while b != 0:
    a, b = b, a % b

print(a)

print("\t------GCD using oneliner----")
from math import gcd
print(gcd(a, b))