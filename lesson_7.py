def guard_zero (operate):
    def inner (x, y):
        if y == 0:
            print("Cannot divide by 0.")
            return
        return operate(x, y)

    return inner


@guard_zero
def divide (x, y):
    return x / y


print(divide(5, 0))  # виводить Cannot divide by 0 («На 0 ділити не можна»)