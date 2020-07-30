i = 10
print("Please enter 10 numbers: ")
l = []
while(i>0):
    l.append(int(input()))
    i-=1
sum = 0
for i in l:
    sum+=i
avg = sum/10
print("The average of 10 numbers is: ",avg)
count = 0
for i in l:
    if i<avg:
        count+=1
print("Total numbers less than average: ", count)
print("The numbers less than average are: ")
for i in l:
    if i<avg:
        print(i)
count = 0
for i in l:
    if i>avg:
        count+=1
print("Total numbers greater than the average are: ", count)
count = 0
for i in l:
    if i==avg:
        count+=1
print("Total numbers equal to average are: ", count)