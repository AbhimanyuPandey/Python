import math
def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
print("Enter a number: ")
n = int(input())
if isPrime(n):
    print("The number is Prime")
else:
    print("The number is not prime")
print("Enter the range for printing prime numbers: ")
a = int(input())
print("The Prime numbers in the entered range are: ")
for i in range(1,a):
    if isPrime(i):
        print(i,end = " ")
print()
