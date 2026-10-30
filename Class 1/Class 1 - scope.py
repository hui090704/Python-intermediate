TAX_RATE = 0.06                      # Global: visible everywhere in this file


def checkout(prices: list[float], member: bool = False) -> float:
    """Return the total to pay.

    prices: item prices in RM
    member: members get 5% off before tax
    """
    total = sum(prices)              # Local: only exists inside checkout()

    def discount(amount: float) -> float:
        rate = 0.05                  # Local to discount()
        return amount * (1 - rate) if member else amount   # 'member' = Enclosing

    return round(discount(total) * (1 + TAX_RATE), 2)       # 'round' = Built-in


print(checkout([10.0, 5.5]))                 # 16.43
print(checkout([10.0, 5.5], member=True))    # 15.61
print(checkout.__doc__.splitlines()[0])      # first docstring line
# print(total) # -> NameError: 'total' only lives inside the function

help(checkout) #help to check function
