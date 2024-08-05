# List:

l= [1,2,3,4,5,1,6,2,'Naga']


x = y = z = "oranges"
print(x)
print(y)
print(z)

x,y,z = "apple","banana","mango"
print(x)
print(y)
print(z)

print(type(l))

print(l)

print(l[-1:])

l.append('babu')
print(l)

print(l[2:-1])

print(len(l))

l.extend([7,8])
print(l)

l.insert(10,9)
print(l)

l.remove(2)
print(l)
l.remove(1)
print(l)

l.pop()
print(l)

index=l[9]
print(index)

count = l.count(3)
print(count)
count = l.count('a')
print(count)

# l.sort()
# print(l)

if "Naga" in l:
    print("Yes,'Naga' is in l")

l[6] = "Venkata"
print(l)

for i in l:
    print(i)

x = "This Is from \"batch-1\" Testing"
print(x)