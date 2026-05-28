print("\t------Check if a string is a palindrome----")
p = "madam"
reversed_str = ""

for char in p:
    reversed_str = char + reversed_str

if p == reversed_str:
    print("Palindrome")
else:
    print("Not Palindrome")

print("\t------Check if a string is a palindrome using oneliner----")
s = "madam"
print(s)
is_palindrome = s == s[::-1]
print(is_palindrome)