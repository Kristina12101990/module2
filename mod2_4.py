numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
i = 0
for i in range(len(numbers)):
    is_prime = True
    if numbers [i] < 2:
      # print(numbers [i], "-не простое, не составное")
          continue
    else:
        f = numbers [i] ** (1/2)
    for a in range(2, int(f + 1)):
        if numbers [i] % a == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes.append(numbers [i])
    else:
        primes.append(numbers [i])
is_prime = True
print('primes = ',primes)
print('not_primes = ',not_primes)