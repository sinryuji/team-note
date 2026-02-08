N = 1000
sieve = [False, False] + [True] * (N-1)
primes = []

for i in range(2, N+1):
    if sieve[i]:
        primes.append(i)
        for j in range(i*2, N+1, i):
            sieve[j] = False

print(primes)