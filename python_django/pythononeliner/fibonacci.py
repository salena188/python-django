print("\t------Calculate fibonacci----")
n = 6
fib = [0, 1]

for i in range(2, n):
    fib.append(fib[-1] + fib[-2])

print(fib[:n])

print("\t------fibonacci using oneliner----")
fib = lambda n: [0,1] if n<=2 else [0,1] + [0]*(n-2)
print(fib(6))