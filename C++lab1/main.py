import math

print(math.exp(1.5))


def t_exp(x: float, eps:float) -> float:
    part = 1
    sum = part
    n = 1
    while abs(part) >= eps:
        part *= x / n
        sum += part
        n += 1
    return sum

print(t_exp(1.5, 0.1**100))

