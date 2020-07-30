print("Even numbers using for loop: ")
for i in range(1, 100):
    if i % 2 != 0:
        pass
    elif i == 10 or i == 20 or i == 30 or i == 40:
        continue
    elif i == 90:
        break
    else:
        print(i)
print("Even numbers using while loop: ")
n = 1
while n <= 100:
    if n % 2 != 0:
        pass
    elif n == 60 or n == 70 or n == 80 or n == 90:
        continue
    elif n == 90:
        break
    else:
        print(n)
    n += 1
