print("Enter a number: ")
a = int(input())
flag = 0
for i in range(2, a//2):
    if a%i==0:
        flag = 1
        break
if(flag == 0):
    print("The number entered is Prime")
else:
    print("The number entered is not Prime")