# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# numbers=[]
# for i in range(2000,3500):
#     if i % 7 ==0 and i % 5 != 0:
#         numbers.append(str(i))
# result=",".join(numbers)
# print(result)

# 2.  Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
#  Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
# number = int(input("Enter a number:"))
# result = fact(number)
# print(result)

# 3. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()

# number=int(input("Enter a number:"))
# numberDict={}
# for i in range(1,number+1):
#     numberDict[i] = i*i
# print(numberDict)

# 4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
# Prompt the user to input a sequence of comma-separated numbers and store it in the 'values' variable

# values ="1,2,32,6,5,4,78,"
# list=values.split(",")
# tuple=tuple(list)
# print('List:',list)
# print('Tuple:',tuple)

#5. Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.
#Hints: Use init method to construct some parameters

class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

# Simple test function
# def test_StringManipulator():
#     sm = StringManipulator()
#     sm.getString()
#     sm.printString()
#
# # Run the test function
# test_StringManipulator()

# 6. Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24

# import math
#
# numbers = input("Provide D: ")
# numbers = numbers.split(',')
#
# result_list = []
# for D in numbers:
#     Q = round(math.sqrt(2 * 50 * int(D) / 30))
#     result_list.append(Q)
#
# print(result_list)

# 7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

# def generate_2d_array(X, Y):
#     # Create a 2D array where each element at (i, j) is i * j
#     return [[i * j for j in range(Y)] for i in range(X)]
#
# # Read input from the console
# input_string = input("Enter two numbers separated by a comma (X,Y): ")
# X, Y = map(int, input_string.split(','))
#
# # Generate the 2D array
# result_array = generate_2d_array(X, Y)
#
# # Print the result
# print(result_array)

#8.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# items = input("Enter words:")
# words = [word for word in items.split(",")]
# print(",".join(sorted(list(set(words)))))

# 9. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
# #Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# def capitalize_lines():
#     print("Enter lines of text. Press Enter on an empty line to finish.")
#
#     lines = []
#
#     while True:
#         line = input()
#         if line == "":
#             break
#         lines.append(line.upper())
#
#     for line in lines:
#         print(line)
#
#
# # Call the function to execute the program
# capitalize_lines()

# 10.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world
#
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. We use set container to remove duplicated data automatically and then use sorted() to sort the data.

# input_string = input("Enter a sequence of whitespace-separated words: ")
# words = input_string.split()
# unique_words = set(words)
# sorted_words = sorted(unique_words)
# result = ' '.join(sorted_words)
# print(result)
