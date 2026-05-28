print("\t------Count vowels----")
s1 = "hello world"
print(s1)
count = 0

for c in s1:
    if c in "aeiouAEIOU":
        count += 1

print(count)

print("\t------Remove vowels----")
s1 = "hello world"
no_vowels = ""

for c in s1:
    if c.lower() not in "aeiou":
        no_vowels += c

print(no_vowels)

print("\t------Count vowel using oneliner----")
s= "pumpkin"
print(s)
count = sum(c in 'aeiouAEIOU' for c in s)
print(count)



print("\t------Remove vowel using oneliner----")
no_vowels = ''.join(c for c in s if c.lower() not in 'aeiou')
print(no_vowels)