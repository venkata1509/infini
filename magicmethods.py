# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f"({self.x},{self.y})"
#     def __repr__(self):
#         return f"point({self.x},{self.y})"
#
# b=point(1,2)
# print(b)
#import sys

# x=15
# print(x.__sub__(9))

# class person:
#     def __init__(self,msg):
#         self.msg=msg
#     def __len__(self):
#         return len(self.msg)
# b=person("Venkata Nagendra Babu Bojja")
# print(len(b))

# class Employe:
#     def __init__(self,string):
#         self.string=string
#
#     def __getitem__(self, index):
#         return self.string[index]
#
# b=Employe({1:'naga',2:'babu',3:'bojja'})
# print(b.string)
# print(f"element is {b[1]}")

# class Employe:
#     def __init__(self,string):
#         self.string=string
#     def __setitem__(self, key, value):
#         self.string[key]=value
# b=Employe({1:'naga',2:'babu',3:'bojja'})
# print(b.string)
# b[1]='Venkata'
# b[2]='Nagendra'
# b[3]='Babu'
# print(b.string)

import sys
# x=[1,2,3,4]
# y=iter(x)
# print(next(y))
# print(sys.getsizeof(y))
# print(next(y))
# # print(sys)

# import sys
# class square:
#     def __init__(self,max):
#         self.max = max
#
#     def __iter__(self):
#         self.current = 0
#         return self
#
#     def __next__(self):
#         if self.current <= self.max:
#             result = self.current**2
#             self.current += 1
#             return result
#         else :
#             raise StopIteration
#
x = square(5)
y = iter(x)
z = next(y)

print(sys.getsizeof(z))
print(z)





