print("\n------Swap----")
a, b = 5, 10
a, b = b, a
print(a, b)

print("\n------If Else----")
age = 20
print("Adult") if age >= 18 else print("Minor")

print("\n------List comprehension----")
squares = [i*i for i in range(1,6)]
print(squares)

print("\n------Even numbers---")
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

print("\n------Reverse string----")
text = "python"
print(text)
print(text[::-1])
'''
print("\n------Read File One-Liner----")
data = open("file.txt").read()
'''
print("\n------Reverse a list----")
numbers = [1,2,3,4]
print(numbers)
print(numbers[::-1])

print("\n------String Manipulation----")
print("\t------Reverse a string----")
string = "hamburger"
print(string)
reversed_str = string[::-1]
print(reversed_str)

print("\t------Check if a string is a palindrome----")
s = "madam"
print(s)
is_palindrome = s == s[::-1]
print(is_palindrome)

print("\t------Count vowels in a string----")
s = "hello world"
print(s)
count = sum(c in 'aeiouAEIOU' for c in s)
print(count)

print("\t------Remove vowels from a string----")
no_vowels = ''.join(c for c in s if c.lower() not in 'aeiou')
print(no_vowels)

print("\t------Capitalize the first letter of each word----")
capitalized = ' '.join(word.capitalize() for word in s.split())
print(capitalized)

print("\n------Numbers & Math----")
print("\t------Calculate factorial----")
from math import prod; factorial = lambda n: prod(range(1, n+1))
print(factorial(5))

print("\t------Check if a number is prime----")
n=7
is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(n**0.5)+1))
print(is_prime(n))

print("\t------Generate Fibonacci numbers (first n)----")
fib = lambda n: [0, 1][:n] + [sum([0, 1][:n][-2:]) for _ in range(n-2)]
print(fib(5))
