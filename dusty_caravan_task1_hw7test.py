#! /usr/bin/env pythons
import sys
from dusty_caravan_task1_hw7 import checkDoors
from urllib.request import urlopen
"""
This script tests the dusty_caravan_task1_hw5.py files method checkDoors
using test input from a csv loaded from the given url.
functions:
    testDoors (loads the url and uses it for the input on running checkDoors)
"""
def testDoors():
    """
    Tests the checkDoors function from the dusty_caravan_task1_hw7.py file
    args: NA
    returns: NA
    """
    tests = urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv")
    tests = tests.read().decode()
    tests = tests.splitlines()
    print(tests)
    count = 1
    for test in tests:
        test = test.replace(' ', '')
        test = test.split(',')
        if test[0] == 'H1':
            pass
        else:
            print("Reading record ", count)
            print("Left dashboard switch (0 or 1):", test[1])
            print("Right dashboard switch (0 or 1):", test[2])
            print("Child lock switch (0 or 1):", test[3])
            print("Master unlock switch (0 or 1):", test[4])
            print("Left inside switch (0 or 1):", test[5])
            print("Left outside switch (0 or 1):", test[6])
            print("Right inside switch (0 or 1):", test[7])
            print("Right outside switch (0 or 1):", test[8])
            print("Gear shift position (P, N, D, 1, 2, 3 or R):", test[9])
            count += 1
            print(checkDoors(test[1], test[2], test[3], test[4], test[5], test[6], test[7], test[8], test[9]))

def main():
    """
    Test Function
    """
    testDoors()
    return

if __name__=="__main__":
    main()
    exit(0)
