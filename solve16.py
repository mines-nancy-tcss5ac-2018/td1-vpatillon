def solve(n):
    """solve the 16th exercise or project Euler :
    return the sum of the digits of 2**n"""

    sum = 0
    power = 2**n
    while power > 0 :
        sum = sum + power % 10
        power = power //10

    return sum

assert( solve(15) == 26)
print("la solution du problème d'Euler n°16 est :" + str(solve(1000)))
