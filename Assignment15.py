a = ["John", "Abhi","Marry","Raj","Kirti"]
print("Enter a name to check if it exists in the list")
s = input()
print("Using Membership operator")
if s in a:
    print("The name exists")
else:
    print("The name does not exist in the list")
print("Without using Membership Operator")
flag = 0
for i in range(0,5):
    if a[i]==s:
        flag = 1
        print("The name exists")
        break
if flag == 0:
    print("The name does not exist in the list")
print("The elements of the list in reverse direction: ")
print(a[::-1])

