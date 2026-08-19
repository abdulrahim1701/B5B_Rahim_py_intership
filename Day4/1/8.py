def require_positive(func):
    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                print("Error: All arguments must be positive.")
                return

        return func(*args)

    return wrapper


@require_positive
def divide(a, b):
    print("Result:", a / b)


divide(10, 2)
divide(10, 0)
divide(-10, 2)