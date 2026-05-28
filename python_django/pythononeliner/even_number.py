print("\n------Even numbers----")
x=int(input("Enter a number: "))
if x%2==0:
    print("even")
else:
    print("odd")


print("\n------Even numbers for range----")
evens = [x for x in range(20) if x % 2 == 0]
print(evens)
