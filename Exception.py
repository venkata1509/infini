# a=15
# b=0
# try:
#     print(a/b)
# except Exception :
#     print("You cannot divisible a number with zero ")

# a=15
# b=0
# try:
#     print(a/b)
# except Exception as e :
#     print("You cannot divisible ",e)

# a=15
# b=0
# try:
#     print("Resource Open")
#     print(a/b)
#     print("Resource closed")
# except Exception as e:
#     print("You cannot ",e)


# a=15
# b=0
#try:
#     print("Resource Open")
#     print(a/b)
# except Exception as e:
#     print("You cannot ",e)
#     print("Resource closed")

# a=15
# b=9
# try:
#     print("Resource Open")
#     print(a/b)
# except Exception as e:
#     print("You cannot ",e)
# finally:
#     print("Resource closed")

# a=15
# b=9
# try:
#     print("Resource Open")
#     print(a/b)
#     v=int(input("Enter a number:"))
#     print(v)
# except Exception as e:
#     print("You cannot ",e)
# finally:
#     print("Resource closed")

a=15
b=9
try:
    print("Resource Open")
    print(a/b)
    v = int(input("Enter a number:"))
    print(v)
except ZeroDivisionError as e:
    print("You cannot ",e)
except ValueError as e:
    print("Invalid Error")
except Exception as e:
    print("Something went wrong")
finally:
    print("Resource closed")