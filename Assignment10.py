print("Enter two numbers")
a = int(input())
temp = a
b = int(input())
a+=b
print("Addition using Assignment operator: ",a)
a = temp
a-=b
print("Subtraction using Assignment operator: ",a)
a = temp
a*=b
print("Multiplication using Assignment operator: ",a)
a = temp
a/=b
print("Division using Assignment operator: ",a)
a = temp
a%=b
print("Modulus using Assignment operator: ",a)
a = temp
a**=b
print("Exponent using Assignment opearator: ",a)
a = temp
a//=b
print("Floor Division using Assignment operator: ",a)