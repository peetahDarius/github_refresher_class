#!/usr/bin/env python

def average(numbers):
    counter = 0
    for number in numbers:
        counter+=int(number)
        ave = counter/len(numbers)
    return ave


numbers = []
while True:
    no = input("Please input your No (or 'done' to finish): ")

    if no == 'done':
        numbers.append(no)
        numbers.remove("done")
        print(numbers)
        answer = average(numbers)
        print("The average of the three numbers is: {0}".format(answer))
        break

    if no.isdigit():
        numbers.append(int(no))
    else:
        print("Invalid input. Please enter a number or 'done' to finish.")

