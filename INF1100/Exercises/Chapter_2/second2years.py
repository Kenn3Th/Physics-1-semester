seconds = 10.0**9
minutes = seconds/60
hours = minutes/60
days = hours/24
years = days/365.25

print 'Can a baby live in %.g s? Yes, it would be %.2f years' % (seconds, years)

"""
Terminal>python second2years.py
Can a baby live in 1e+09 s? Yes, it would be 31.69 years
"""
