print("\t------Ternary conditional ----")
x = 15
if x > 10:
    result = "Yes"
else:
    result = "No"

print(result)
print("\t------Ternary conditional using oneliner----")
result = "Yes" if x > 10 else "No"
print(result)


print("\n\t------Checks All elements are unique ----")
lst = [1,2,3,4,5]
unique = True

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            unique = False

print(unique)
print("\t------Checks All elements are unique using oneliner----")
unique = len(set(lst)) == len(lst)
print(unique)


print("\n\t------Check if two lists are anagrams ----")
# anagrams :  word or phrase formed by rearranging the letters of a different word cinema ==iceman
list1 = ['a','b','c']
list2 = ['c','b','a']

list1.sort()
list2.sort()

print(list1 == list2)
print("\t------Check if two lists are anagrams using oneliner----")
are_anagrams = sorted(list1) == sorted(list2)
print(are_anagrams)


print("\n\t------Check if all elements in the list are true ----")
all_true = True
for x in lst:
    if not x:
        all_true = False
print(all_true)

print("\t------Check if all elements in the list are true using oneliner----")
print(all(lst))

print("\n\t------Check if any element is true ----")
any_true = False
for x in lst:
    if x:
        any_true = True
print(any_true)

print("\t------Check if any element is true using oneliner----")
print(any(lst))