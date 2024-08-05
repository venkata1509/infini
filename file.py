# 1. Write a Python program to read the contents of a text file named input.txt and display them on the screen.

# filepath="E:\Infinitude\Ass\python2.txt"
# v=open(filepath,"r")
# print(v.read())

# 2. Write a Python program to take user input and write it to a new text file named output.txt.

# f="E:\Infinitude\Assignments\output.txt"
# input=input("Enter a text you want:")
# b=open(f,"w")

# 3. Write a Python program to copy the contents of one text file named source.txt to another text file named destination.txt.

# import shutil
# src_path=r"E:\Infinitude\Assignments\source.txt"
# dst_path=r"E:\Infinitude\Assignments\destination.txt"
# shutil.copy(src_path,dst_path)
# print("copied")

# 4.Write a Python program to read data from a CSV file named data.csv and display it in tabular format.
#

# import csv
# import pandas as pd
# from tabulate import tabulate
#
#
# f=open('people.csv', 'r')
# # df= csv.reader(f)
# df=pd.read_csv(f)
# print(tabulate(df , headers='keys', tablefmt='grid'))

# import json
#
# def read_json(file_path):
#     with open(file_path,"r") as file:
#         data = json.load(file)
#         return data
# json_data="C:\users\hp\PycharmProject\pythonProject\\numpy\\1.json"
# print((json_data))

