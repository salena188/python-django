print("\t------Sum of square ----")
n = 5
sum_sq = 0

for i in range(1, n + 1):
    sum_sq += i * i

print(sum_sq)

print("\t------Sum of square using oneliner----")
sum_sq = sum(i*i for i in range(1, n+1))
print(sum_sq)