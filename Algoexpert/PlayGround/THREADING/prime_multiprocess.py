import concurrent.futures
import math
import time

start = time.perf_counter()
print(f" start time {start}")

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
    #with concurrent.futures.ThreadPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f"{number} is prime {prime}")

if __name__ == "__main__":
    main()

finish = time.perf_counter()
#print(f"end time {finish}")
print(f"Finished in {round(finish-start, 2)} seconds")
