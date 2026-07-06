#!/usr/bin/env python3

print('Welcome to the age calculator.')
answer = input('Would you like to know how old you will be in a particular year? (y/n)')

while not (answer == 'y' or answer == 'n'):
    print("The value of answer is", answer)
    print("I'm sorry, I didn't understand. Please try again.")
    answer = input('Would you like to know how old you will be in a particular year? (y/n)')

if answer == 'n':
    print("I'm sorry you're not interested. Goodbye!")
else:
    dates = []
    print("Valid formats for dates: '1/1/2000' or 'jan 1, 2000'")
    dob = input('What is your birthday? ')
    dates.append(dob)
  
    future = input('What date did you want to know about?')
    dates.append(future)

    month = ['', '']
    day = ['', '']
    year = ['', '']
    counter = 0
    for date in dates:
        if dates[counter][0].isdigit() is True:
            tempDate = date.split('/')
            month[counter] = tempDate[0]
            year[counter] = tempDate[2]
            day[counter] = tempDate[1]
        else:
            tempDate = date.split()
            month[counter] = tempDate[0]
            year[counter] = tempDate[2]
            for i in tempDate[1]:
                if i != ',':
                    day[counter] = day[counter] + i
        counter += 1
            
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
   
    if month[0][0:3].lower() in months:
       month[0] = months.index(month[0][0:3].lower())
    if month[1][0:3].lower() in months:
       month[1] = months.index(month[1][0:3].lower())

    month[0] = int(month[0])
    month[1] = int(month[1])
    
    age = int(year[1]) - int(year[0])
    day[0] = int(day[0])
    day[1] = int(day[1])
    if month[1] <= month[0]:
        age = age - 1
        if month[1] == month[0]:
            if day[1] >= day[0]:
                age = age + 1

    results = 'On {} you will be {} years old.'

    print(results.format(dates[1], age))
    print('Goodbye!') 