a = [1,2,3,4,5,6,7,8,9,10]
b = ["John", "Abhi","Marry","Raj","Rahul","Riya","Simran","Kirti","Yash","Sonu"]
print("All names are: ")
for i in b:
    print(i)
print("Enter an index: ")
index = int(input())
print("Employee id: ",a[index])
print("Employee name: ",b[index])
print("Names from 4th position to 9th position are: ")
print(b[3:9])
print("Names from third position are: ")
print(b[2:])
print(" Enter number of times of repetition: ")
n = int(input())
print(b*n)
print("The concatenation of the lists is: ")
print(a+b)
print("Side by Side elements od the lists: ")
for i in range(0,10):
    print(a[i],end = " ")
    print(b[i], end = " ")
print()