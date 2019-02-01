def triangle_area(vertices): # formula for the area of a triangle
    v = vertices
    pulk = (v[1][0]*v[2][1]) - (v[2][0]*v[1][1]) - (v[0][0]*v[2][1]) + \
      (v[2][0]*v[0][1]) + (v[0][0]*v[1][1]) - (v[1][0]*v[0][1])
    return (1.0/2.0)*abs(pulk)

v1 = (0,0); v2 = (1,0); v3 = (0,2)
vertices = [v1, v2, v3]
    
def test_triangle_area(): # test function for the computed formula
    """
    Verify the area of a triangle with vertex coordinates
    (0,0), (1,0), and (0,2).
    """
    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = (expected - computed) < tol
    msg = 'computed area=%g != %g (expected)' % (computed, expected)
    assert success, msg

test_triangle_area() # call for the test function

"""
Did not get msg when I run the program. Therfor the function past the test.
Have also tried changing a number in the test function and checked.
"""
