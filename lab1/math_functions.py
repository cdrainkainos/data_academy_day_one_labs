def add(x, y):
    if isinstance(x, int) or isinstance(y, int):
        return "At least one number is non-numeric"
    else:
        return x + y