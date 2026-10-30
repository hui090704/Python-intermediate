# A function is a named, reusable recipe: input -> work -> output


def add_sst(price):
    """Return the price with 6% SST added."""
    return round(price * 1.06, 2)


def greet(name):
    """Print a welcome message. Returns nothing (None)."""
    return(f"Selamat datang, {name}!")


total = add_sst(10.00)
print(total)              # 10.6
print(add_sst(25.50))     # 27.03

greet("Aisyah")
result = greet("Darren")
print(result)             # None, because greet() has no return