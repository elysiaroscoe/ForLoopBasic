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

for fours in range (2018, 0, -4): #making the 4 negative wasn't intuitive to me, I assumed it would run the range
    print(fours)


lowNum = 0
highNum = 56
mult = 3
for y in range(lowNum, highNum + 1):
    if y % mult == 0:
        print(y)