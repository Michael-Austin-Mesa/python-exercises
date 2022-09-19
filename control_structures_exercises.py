#Q1a
dotw = input('Enter a day (please capitalize): ') #dotw = day of the week
if dotw == 'Monday':
    print(f'Today is {dotw}')
else:
    print('It is not Monday')
#Q1b
dotw = input('Enter a day (please capitalize): ')
#dotw = 'Tuesday'
if dotw == 'Saturday' or dotw == 'Sunday':
    print(f'Today is {dotw}, the weekend')
else:
    print(f'It is {dotw}, a weekday')
#Q1c
hours_weekly = 50
hourly_rate = 15
weekly_pay = hourly_rate * hours_weekly
if hours_weekly > 40:
    weekly_pay = weekly_pay * 1.5
    print(f'Time and a half pay this week is {weekly_pay}')
else:
    print(f'Base pay this week is {weekly_pay}')

#Q2a while loops
i = 5
while i <= 15:
    print(i)
    i += 1

#i = 0
i = 100
while i >= -10: # <= 100:
    print(i)
    #i += 2
    i -=5

i = 2
while i <= 1000000:
    print(i)
    i = i**2

i = 100
while i >= 5:
    print(i)
    i -= 5

#Q2b for loops
i = int(input('Enter a number: '))
result = 0
for j in range(1,11):
    result = i * j
    print(f'{i} x {j} = {result}')

rows = 10
for r in range(rows):
    for s in range(r):
        print(r,end='')
    print('')

#Q2c break and continue
i = 10
for n in range(i):
    print(i)
    i -= 1
    if i < 1:
        break

n = int(input('Enter a positive integer: '))
if n > 0:
    for i in range(0,n+1):
        print(i)
        i += 1
       if i == n+1:
           break

#this one needs work

#m = input('Enter an odd number between 1 and 50 to skip: ')

while True:
    m = input('Enter an odd number between 1 and 50 to skip: ')
    if m.isdigit():
        m = int(m)
        if m%2 == 0:
            print('Not an odd number.')
            continue
        else:

            for i in range(0,50):
                if i == m:
                    print(f"Skipping {i}")
                elif i%2 == 1:
                    print(f'Here is an odd number: {i}')
    else:
        print('Not a number.')



#Q3 FizzBuzz
while i <= 100:
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
        i += 1
    elif i%5 == 0:
        print('Buzz')
        i += 1
    elif i%3 == 0:
        print('Fizz')
        i += 1
    else:
        print(i)
        i += 1

#Q4 Display table of powers

while True:
    i = int(input('Enter integer to go up to: '))
    for j in range(0,i+1):
        print(f'Number: {j}')
        print(f'Number Squared: {j**2}')
        print(f'Number Cubed: {j**3}')
        
    m = input('Do you want to continue? y/n: ')
    if m == 'n':
        break
    elif m == 'y':
        continue


