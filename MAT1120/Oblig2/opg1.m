A = [
    1 1 0 2
    0 1 0 1
    1 0 0 1
    1 0 1 2];
y = [
    1
    1
    1
    1];
AT = transpose(A);

x = rats(inv(AT*A)*AT*y)