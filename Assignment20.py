print("Enter the range:")
n = int(input())
sum = 0
first = 0
sec = 1
i = 1
print("Fibonacci series up to the entered range is :  ")
print(first,end =" ")
while i<n:
    sum = first+sec
    print(sum,end = " ")
    first = sec
    sec = sum
    i+=1
print()
print("Enter the max number in the fibonacci sequence: ")
m = int(input())
sum = 0
first = 0
sec = 1
i = 1
print("The sequence up to the entered number is : ")
print(first,end =" ")
while sum<m:
    sum = first + sec
    print(sum, end=" ")
    first = sec
    sec = sum
