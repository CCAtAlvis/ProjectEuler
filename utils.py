def isPrime (num):
    i = 2
    while i*i <= num:
        if num%i == 0:
            return False
        i += 1
    return True


def primes(number):
    primes = [2]
    primes += [i for i in range(3,number+1,2)]

    i = 3
    while i*i <= number:
        if i in primes:
            for j in range(i*2, number+1, i):
                if j in primes:
                    primes.remove(j)
        i += 1

    return primes

print(primes(1000))
