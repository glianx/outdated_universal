def return_primes():
    primes = []
    for x in range(2,311):
        for i in range(2,x):
            if x % i == 0:
                break
        else:
            primes.append(x)
    return primes

primes = return_primes()

for prime in primes:
    print(bin(int(prime ** (1./3) % 1 * 2**32)))