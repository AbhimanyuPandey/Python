print("Printing numbers using for loop:")
for i in range(1,101):
    print(i,end = " ")
print()
for i in list(range(1,101))[::-1]:
    print(i, end = " ")
print()
print("Printing numbers using while loop:")
i = 1
while i<101:
    print(i, end = " ")
    i+=1
print()
i = 100
while i >0:
    print(i, end = " ")
    i-=1
print()
mystring = "Hello World"
print("Printing characters in my string: ")
for i in mystring:
    print(i)