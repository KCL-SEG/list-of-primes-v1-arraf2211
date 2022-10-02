"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    x = 3
    if number_of_primes > 0:
        list.append(2)
        while len(list) < number_of_primes:
            flag = False
            for i in range(2, x):
                if x % i == 0:
                    flag = False
                    break
                else:
                    flag =True
            if flag:
                list.append(x)
            x = x + 1


    return list
