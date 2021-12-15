def gcd(m, n):
    while m % n != 0:
        old_m, old_n = m, n
        m = old_n
        n = old_m % old_n
    return n


print(gcd(121, 11))

