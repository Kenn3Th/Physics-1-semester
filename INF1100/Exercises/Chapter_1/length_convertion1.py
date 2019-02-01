"""
formula:
length_in_unit = length_in_meter/unit
length_in_km = length_in_meters/1000
"""
inch = 2.54/100
foot = 12*inch
yard = 3*foot
bmile = 1760*yard

print '''one inch is %g meters, one foot is %g meters,
one yard is %g meters, one british mile is %g meters.''' %(inch, foot, yard, bmile)

length_in_meter = 640.0

length_in_inches = length_in_meter/inch
length_in_feet = length_in_meter/foot

print '''This is the vertification of my calculations.
%g meters is %g inches and %g feet''' % (length_in_meter, length_in_inches, length_in_feet)

"""
Terminal>In [11]: run length_convertion1.py
one inch is 0.0254 meters, one foot is 0.3048 meters,
one yard is 0.9144 meters, one british mile is 1609.34 meters.
This is the vertification of my calculations.
640 meters is 25196.9 inches and 2099.74 feet
"""
