
def sum_1k(M):
    """Dette er formelen for alle matematiske summe formlene"""
    s = 0
    for k in range(1, M+1):
        s += 1.0/k
    return s

def test_sum_1k():
    expected = 1.0 + 1.0/2 + 1.0/3
    computed = sum_1k(3)
    tol = 1e-10
    success = abs(expected - computed) < tol
    msg = "Expected %g, got %g" %(expected, computed)
    assert success, msg

test_sum_1k()
