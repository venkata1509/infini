# # Defining a function
# def fun(firstname,lastname):
#     print("Firstname:" +firstname+" , "+"Lastname:"+lastname)
# fun("Naga","bojja")
#
# def my_fun(cars):
#     for x in cars:
#         print(x)
# cars=["Tesla","TATA"]
# my_fun(cars)
#
# def multiarg(*args):
#     print("Nagendra Argument" +args[1])
# multiarg("test1","test2","test3","test4")
#
# *args which is for arbitary number of number and ** keyword arguments arbitary number of arguments
#  def keyarg(**kwargs):
#     print("keyword Args",kwargsarg["test1"])
# keyarg(test1="Venkata",test2="Nagendrababu",test="Bojja")

## Lambdaq functions

# x = lambda a,b: a * b
# #x = lambda a,b : a+b
# print(x(5,4))
#print(x(5,4))

## Return vlaues

# def my_fun(x):
#     return 5 * x
# print(my_fun(80))

# def my_fun(fname):
#     print(fname + " Bojja ")
# my_fun("Venkata")
# my_fun("Nagendra")
# my_fun("Babu")

# def fun(username, password):
#     print("first function")
#     print(username)

# def test(text):
#     return text.upper()
# def test2(text):
#     return text.lower()
# def test1(fun):
#     test = fun("This is from inner function")
#     print(test)
# test1(test)
# test1(test2)

# def add(*args):
#     total =0
#     for num in args:
#         total +=num
#     return total
# print(add(1,2,3,4))
# print(add(1,2,3,4,5,6,7,8))

# import paramiko
# def ssh_connect(host,username,password,port):
#     try :
#         client = paramiko.SSHClient
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(hostname=host,username=username,password=password,port=port)
#         print("connection is successful")
#     except Exception as e:
#         print(f"Error: {e}")
# # ssh_connect(host="192.168.196.35",username="root",password="naga1509",port="22")
# #







