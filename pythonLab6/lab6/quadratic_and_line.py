

def quadratic(a, b, c):
    if a == 0:
        raise ValueError('Please provide a - coefficients different than zero') # dlaczego?
    delta = b**2 - 4*a*c
    if delta < 0:
        return ()
    elif delta == 0:
        return [-b / (2 * a)]
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return (x1, x2)




def linear(xy1, xy2):
    if xy1[0] == xy2[0] and xy1[1] == xy2[1]:
        raise ValueError("Points (x1, y1) and (x2, y2) are equals")
    a = (xy1[1] - xy2[1]) / (xy1[0] - xy2[0])   # ZeroDivisionError
    b = xy1[1] - xy1[0] * (xy1[1] - xy2[1]) / (xy1[0] - xy2[0])
    return [a, b]

quadratic(3, 3, -18)    # do usunięcia
