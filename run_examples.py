
s = "jajkfhdjbaoioiebcjhb"
count = 0

for x in s:
    if x in "aeiou":
        count+=1
print(count)

d = "aeiou"

c = 0
for x in s:
    if x in d:
        c+=1
print(c)

print(list(s))

y = dict()
t = list(s)
z = []
for x in t:
    if x in "aeiou":
        y[x] = y.get(x, 0) + 1
for x,y in y.items():
    z.append( (y,x) )

#z.sort()

for x in z:
    print(x)



s = 'azcbobobbegbobghakl'

counter = 0
index = 0
while index < len(s):
    index = s.find("bob", index)
    if index == -1:
        break
    print("bob found at", index)
    counter +=1
    index += 2
print("Number of times bob occurs is:", counter)

# import regex as re
#
# x = re.findall("bob", s, overlapped=True)
# print("Number of times bob occurs is:",len(x))





# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
# Longest substring in alphabetical order is: abc

for i in range(5):
    print(i)


a = 2*2
print(f"Hello World {a}\nI Love you!")

x = 2
y = 5

# x = int(input("Please enter x value: "))
# y = int(input("Please enter y value: "))

print(f"{x} * {y} = {x * y}!\n Well done!")

print(2/10 == 0.3)
