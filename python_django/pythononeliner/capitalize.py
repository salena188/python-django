print("\t------Capitalize----")
s = "hello world python"
words = s.split()
result = []

for word in words:
    result.append(word.capitalize())

capitalized = " ".join(result)
print(capitalized)

print("\t------Capitalize using onliner----")
s2="its the end of world"
capitalized = ' '.join(word.capitalize() for word in s2.split())
print(capitalized)