#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: March 2, 2025
# This program uses one for loop and one if statement and
# Prints the integers from 1000 to 2000,


def main():
    for number in range(1000, 2001):
        print(number, end=" ")
        if number % 5 == 4:
            print()


main()
