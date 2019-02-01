def max(a):
    max_elem = a[0]

    for elm in a[1:]:
        if elm > max_elem:
            max_elem = elm
            
    return max_elem

def min(a):
    min_elem = a[0]

    for elm in a[1:]:
        if elm < min_elem:
            min_elem = elm
    return min_elem

test = [5,6,-2,7,54,-7,0,9,4]

print max(test)
print min(test)

"""
Terminal>python maxmin_list.py 
54
-7
"""
