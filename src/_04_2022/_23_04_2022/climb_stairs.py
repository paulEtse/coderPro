def staircase(n):
    """
    fibo
    solution https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
    """
    if n <= 0:
        return 0
    if n in [1, 2]:
        return n
    n_1 = 1
    n_2 = 2

    for i in range(2, n):
        aux = n_2
        n_2 = n_2 + n_1
        n_1 = aux
    return n_2
