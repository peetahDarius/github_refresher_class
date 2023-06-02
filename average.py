#!/usr/bin/env python


def average(x,y,z):
	a=(x+y+z)/3
	return a

x = input("please put in number1: ")
y = input("please put in number2: ")
z = input("please put in number3: ")


answer = average(x,y,z)
print("The average of the three numbers is: {0}".format(answer))
