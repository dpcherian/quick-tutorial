import numpy as np
import matplotlib.pyplot as plt


# Code file by Philip on Jan 23rd, 2022
# Simple Python program file


print("This is a program that prints a random number between 1 and a number of your choice")

print("Insert maximum number")
max_n = input()

n = np.random.randint(max_n)

print(n)

# End of the program
