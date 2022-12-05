def primes_generator():
    current_number = 2
    while True:
        yield current_number
        current_number += 1 if current_number == 2 else 2
        while True:
            check = False
            for i in range(2, int(current_number ** 0.5) + 1):
                if current_number % i == 0:
                    current_number += 2
                    check = True
                    break
            if not check:
                break


if __name__ == '__main__':
    my_primes = primes_generator()
    for i in range(9):
        print(next(my_primes))
