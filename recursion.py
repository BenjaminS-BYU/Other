# def walk(steps):
#     if steps <= 0:
#         return
#     walk(steps - 1)
#     print(f"Step {steps}")

# walk(5)


def factorial(x):
    result = 1
    if x > 0:
        for y in range(1, x + 1):
            result *= y
    return result

print(factorial(10))


def factorial_recursive(x):
    if x <= 1:
        return 1
    else: 
        return x * factorial_recursive(x - 1)

print(factorial_recursive(10))