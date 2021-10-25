for i in range (151):
    print(i)

for x in range (5,1001,5):
    print(x)

for num in range (1,101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

sum = 0
for int in range (0,500001):
    if int % 2 != 0:
        sum += int
print(sum)
