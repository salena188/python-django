print("\t------Calculate factorial----")
n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)

print("\t------factorial using oneliner----")
from math import prod
factorial = lambda n: prod(range(1, n+1))
print(factorial(5))