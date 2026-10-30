def make_receipt(customer, *items, discount=0.0, **notes):
    """Print a receipt. Each item is a (name, price) pair."""
    subtotal = sum(price for _, price in items)
    total = subtotal * (1 - discount)
    print(f"Customer: {customer}")
    for name, price in items:
        print(f"  {name:<12} RM{price:>6.2f}")
    if discount:
        print(f"  {'Discount':<12} {discount:>8.0%}")
    print(f"  {'TOTAL':<12} RM{total:>6.2f}")
    for key, value in notes.items():
        print(f"  note - {key}: {value}")
    print()


# positional argument + any number of items (*items)
make_receipt("Aisyah", ("Teh Tarik", 3.00), ("Roti Canai", 2.50))

# keyword argument (discount=) + extra keyword notes (**notes)
make_receipt("Darren", ("Nasi Lemak", 6.50), ("Kopi O", 2.50),
             discount=0.10, table=4, sugar="less")

make_receipt("Darren", ("Nasi Lemak", 6.50), ("Kopi O", 2.50), ("Nasi Goreng", 4.50), ("Mi Rebus", 5.50),
             discount=0.2, table=4, sugar="less", cahier="Nurin")