numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i > 1:
        for j in range(0,len(numbers)):
            if i % j == 0:
                break
        else:
            primes.append(i)
        if i not in primes:
            not_primes.append(i)
print('Primes: ', primes)
print('Not primes: ', not_primes)











