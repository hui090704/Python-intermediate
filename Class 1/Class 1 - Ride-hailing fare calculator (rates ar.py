# Ride-hailing fare calculator (rates are made up for practice)
# Fill in the TODOs, then run. All 5 checks must print OK.

BASE_FARE = 2.00
PER_KM = 0.80
PER_MIN = 0.20
MINIMUM_FARE = 6.00


def fare(km: float, minutes: float, surge: float = 1.0) -> float:
    """Return the trip fare in RM, never below the minimum fare."""
    # TODO 1: base + km cost + time cost
    price = BASE_FARE + km*PER_KM + minutes*PER_MIN
    # TODO 2: multiply by surge
    price *= surge
    # TODO 3: apply the minimum fare, round to 2 decimals
    return round(max(price, MINIMUM_FARE),2)


def with_promo(amount: float, code: str = "") -> float:
    """Apply a promo code: 'JOM5' = RM5 off, 'HALF' = 50% off (max RM10)."""
    # TODO 4
    if code=="JOM5":
        amount -= 5
    elif code=="HALF":
        amount = amount - min(amount*0.5, 10)

    return amount


checks = [
    (fare(5, 10), 8.00),
    (fare(1, 3), 6.00),                 # minimum fare applies
    (fare(5, 10, surge=1.5), 12.00),
    (with_promo(12.00, "JOM5"), 7.00),
    (with_promo(30.00, "HALF"), 20.00),  # 50% capped at RM10
]
for got, expected in checks:
    print("OK  " if got == expected else "FIX ", got, "expected", expected)