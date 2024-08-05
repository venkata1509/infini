#1.
#Write a python program to print only dictionary keys and values separately.Take a dictionary with 5 items (Key-Value Pairs)

dict = {
    "name": "Nagendra",
    "age": 22,
    "city": "guntur",


    "profession": "Engineer",
    "hobby": "Reading"
}
print(type(dict))
print(dict)

#a. From the above dictionary pop or remove the last element
# last_ele = dict.popitem()
# print(last_ele)
# #b. Take dictionary from 1.a and add the following key & pair i;e "car":"Tesla" to the dictionary if the key exsists then it should update the value otherwise it should add the Key

dict = {
    "name": "Nagendra",
    "age": 22,
    "city": "guntur",
    "profession": "Engineer",
    "hobby": "Reading"
}

key = 'car'
value = 'Tesla'

if key in dict:
    dict[key]=value
else:
    dict[key]=value
print(dict)

#c.Convert the dictionary to List

tuple = tuple(dict.items())
print(tuple)

# 2 .
#  Create a list of length 10 including numbers and strings
l=[1,'Venkata',2,'Nagendra',3,'Babu',4,'Bojja',5,'Ramarao']
print(type(l))
# 	a. Slice the list till the index 8
print(l[:8])
# 	b. Print the element which is located at index 8
index =l[8]
print(index)
# 	c. Perform sort and reverse operations on the list

l.reverse()
l.sort(key=lambda x:str(x))
print(l)

# 	d. Write a program which takes string as input and reverses that string
#
s=input("Enter a string:")
reversed_string=s[::-1]
print("Reversed string:",reversed_string)

# 3. Write a program which prints numbers in range 1,100 which are divisible by 5

for i in range(1,101 ):
    if(i % 5 ==0):
        print("Numbers are:",i)

