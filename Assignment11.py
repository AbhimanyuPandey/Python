print("Enter two numbers: ")
a = int(input())
b = int(input())
res = a&b
print("Bitwise AND of two numbers: ", res)
res = a|b
print("Bitwise OR of two numbers: ", res)
res = a^b
print("Bitwise XOR of two numbers: ", res)
res = ~a
print("Bitwise NOT of first number: ", res)
res = b<<2
print("Bitwise Left shift of 2 bits of second number: ", res)
res = a>>3
print("Bitwise Right shift of 3 bits of first number: ", res)


