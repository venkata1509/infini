#recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
n=5
print("Factorial of n is:",factorial(n))
