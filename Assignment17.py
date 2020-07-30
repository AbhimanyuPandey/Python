print("Enter total N: ")
N = int(input())
l = []
while(N>0):
    l.append(int(input()))
    N-=1
print("The maximum of numbers entered is :", max(l))
print("The minimum of numbers entered is: ",min(l))