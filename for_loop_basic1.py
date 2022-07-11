# Basic
for i in range (0,151):
    print(i)


# Multiples of 5
count = 5 
while count < 1001:
    print(count)
    count+=5

# Counting the Dojo Way 
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print  ("Coding")
    else:
        print(i)

#Adding Integers from 0 to 500,000
sum = 0 
for i in range(0,500001):
    if(i % 2 != 0): 
        sum += i
print(sum)

#Count down by 4s from 2018 

count = 2018
while count > 0:
    print(count)
    count -= 4

#Flexible Counter

lowNum = 15
highNum = 50
mult = 9 

for i in range (15, 51):
    if i % mult == 0:
        print(i)