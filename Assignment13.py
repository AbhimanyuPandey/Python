print("Enter 5 numbers: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a>b:
    if a>c:
        if a>d:
            if a > e:
                print("The greatest number is: ",a)
            else:
                print("The greatest number is: ",e)
        elif d>e:
           print("The greatest number is: ", d)
        else:
            print("The greatest number is: ", e)
    elif c>d:
        if c>e:
            print("The greatest number is: ", c)
        else:
            print("The greatest number is: ", e)
    else:
        if d>e:
            print("The greatest number is: ", d)
        else:
            print("The greatest number is: ", e)
elif b>c:
    if b>d:
        if b>e:
            print("The greatest number is: ", b)
        else:
            print("The greatest number is: ", e)
    elif d>e:
        print("The greatest number is: ", d)
    else:
        print("The greatest number is: ", e)

elif c>d:
   if c>e:
       print("The greatest number is: ", c)
   else:
       print("The greatest number is: ", e)
else:
    if d>e:
        print("The greatest number is: ", d)
    else:
        print("The greatest number is: ", e)

