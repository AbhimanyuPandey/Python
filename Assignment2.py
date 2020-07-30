print("Enter three numbers")
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    print("The greatest among the three numbers is: ", a)
elif b>a and b>c:
    print("The greatest among the three numbers is: ", b)
else:
    print("The greatest among the three numbers is: ", c)