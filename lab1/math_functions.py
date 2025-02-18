def add(x, y):
    if isinstance(x, int) or isinstance(y, int):
        return x + y
    else:
        return "At least one number is non-numeric"