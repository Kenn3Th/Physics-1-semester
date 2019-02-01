def h(x):
    if x < 0:
        value = 0
    elif x >= 0: 
        value = 1
    return value

def test_h():
    q = h(-10e-15)
    expected_values = [0, 0, 1, 1, 1]
    computed_values = [-10, -10e-15, 0, 10e-15, 10]
    for expected, computed in zip(expected_values, computed_values):
        msg = 'computed =%g != %g (expected)' %(computed, expected)
        assert expected == h(computed)

test_h()

H = h(-10)
k = h(-10e-15)
t = h(0)
u = h(10e-15)
b = h(10)

print H, k, t, u, b

"""
Terminal>python Heavside.py 
0 0 1 1 1
"""
