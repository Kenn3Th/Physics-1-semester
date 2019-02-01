import random
import numpy as np

def roll_dice(n):
    s = []
    for i in xrange(n):
        r = random.randint(1,6)
        g = random.randint(1,6)
        s.append(r + g)
    return s
"""
def sums(roll_dice):
    rd = roll_dice
    sums = [
        two = []
        three = []
        four = []
        five = []
        six = []
        seven = []
        eight = []
        nine = []
        ten = []
        eleven = []
        twelve = []
    [
    if rd == 2:
        two.append(rd)
    elif rd == 3:
        three.append(rd)
    elif rd == 4:
        four.append(rd)
    elif rd == 5:
        five.append(rd)
    elif rd == 6:
        six.append(rd)
    elif rd == 7:
        seven.append(rd)
    elif rd == 8:
        eight.append(rd)
    elif rd == 9:
        nine.append(rd)
    elif rd == 10:
        ten.append(rd)
    elif rd == 11:
        eleven.append(rd)
    elif rd == 12:
        twelve.append(rd)
    return sums
"""
n = 30
lst = np.sort(roll_dice(n))
print lst

result = {}
result =


two = []; three = []; four = []; five = []; six = []; seven = []
eight = []; nine = []; ten = []; eleven = []; twelve = []
for rd in lst:
    if rd == 2:
        two.append(1)
    elif rd == 3:
        three.append(1)
    elif rd == 4:
        four.append(1)
    elif rd == 5:
        five.append(1)
    elif rd == 6:
        six.append(1)
    elif rd == 7:
        seven.append(1)
    elif rd == 8:
        eight.append(1)
    elif rd == 9:
        nine.append(1)
    elif rd == 10:
        ten.append(1)
    elif rd == 11:
        eleven.append(1)
    elif rd == 12:
        twelve.append(1)
print two, three, four, five, six, seven, eight, nine, ten, eleven, twelve 
