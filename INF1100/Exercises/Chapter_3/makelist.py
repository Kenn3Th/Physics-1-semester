def makelist(start, stop, inc):
    value = start
    result =[]
    while value <= stop:
        result.append(value)
        value = value + inc
    return result

mylist = makelist(0, 100, 5)
import pprint
pprint.pprint(mylist)
