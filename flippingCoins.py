# Walker Gentz
# CSCI 195
# Homework 20

import random

def flipCoin():
    if random.randint(0,1) == 1:
        return "H"
    else:
        return "T"

def flipCoinNum(n):
        flipArray = [0]*n
        i = 0
        while i < n:
            flipArray[i] = flipCoin()
            i = i + 1
        return flipArray
    
def findStreak(arr, s):
    i = len(arr)-1
    repeated = 1
    repeatedFinal = 0
    while i > 0:
        if arr[i] == arr[i-1] == s:
            repeated = repeated + 1
            repeatedFinal = repeated
            i = i - 1
        else:
            repeated = 1
            i = i - 1
    return repeatedFinal

def main():
    print("Let's Flip Some Coins\n")
    print("1) Flip a coin one time")
    print("2) Flip a coin n times and show the flips")
    print("3) Flip a coin n times and show the ratio of heads and tails")
    print("4) Flip a coin n times and show the longest run of heads and tails")
    print("5) Likelihood of a run of 4 or more heads with 20 flips")
    menuNum = int(input("Selection: "))
    if menuNum == 1:
        x = flipCoin()
        if x == "H":
            print("Heads")
        else:
            print("Tails")
    elif menuNum == 2:
        numFlip = int(input("How many flips: "))
        x = flipCoinNum(numFlip)
        print(*x)
    elif menuNum == 3:
        numFlip = int(input("How many flips: "))
        x = flipCoinNum(numFlip)
        heads = 0
        tails = 0
        for n in x:
            if n == "H":
                heads = heads + 1
            else:
                tails = tails + 1
        print(*x)
        print("Number of Heads: " + str(heads))
        print("Number of Tails: " + str(tails))
        print("The Head/Tail ratio: " + str(float(heads/tails)))
    elif menuNum == 4:
        numFlip = int(input("How many flips: "))
        x = flipCoinNum(numFlip)
        if numFlip <= 30:
            print(*x)
        repeatHead = findStreak(x, "H")
        repeatTail = findStreak(x, "T")
        print("Longest Run Heads: " + str(repeatHead))
        print("Long Run Tails: " + str(repeatTail))
    elif menuNum == 5:
        numEx = int(input("Number of times to run the experiment: "))
        i = 1
        success = 0
        while i <= numEx:
            x = flipCoinNum(20)
            if findStreak(x, "H") >= 4:
                success = success + 1
            i = i + 1
        pct = success/numEx
        print("The likeihood with " + str(numEx) + " experiments: " + str(pct*100) + "%")
    else:
        print("Invalid Selection - Program Terminated")
        
main()
