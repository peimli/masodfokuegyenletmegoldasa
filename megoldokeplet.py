import math
def masodfoku(a,b,c):
    if (b**2 - 4 * a * c) < 0:
        return None
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1, x2
