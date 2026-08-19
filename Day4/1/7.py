import time

def timer(func):
    def wrapper():
        start = time.time()

        result = func()

        end = time.time()
        print("Time taken:", end - start, "seconds")

        return result

    return wrapper


@timer
def calculate_sum():
    total = 0

    for i in range(1, 1000001):
        total += i

    print("Sum:", total)


calculate_sum()