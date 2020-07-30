import sys

for i in range(1, len(sys.argv)):
    print((sys.argv[i]))
max = -999999999
for i in range(1, len(sys.argv)):
    if int(sys.argv[i])>max:
        max = int(sys.argv[i])
print(" The greatest number among the numbers is: ",max)