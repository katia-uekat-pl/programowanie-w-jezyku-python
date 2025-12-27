def calculate_discount(price: float, discount: float) -> float:

    if not (0.0 <= discount <= 1.0):
        raise ValueError("Discount must be between 0 and 1 (inclusive).")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    final_price = price * (1 - discount)

    return float(final_price)


print(calculate_discount(100, 0.2))
print(calculate_discount(50, 0))
print(calculate_discount(200, 1))

try:
    calculate_discount(100, -0.1)
except ValueError as e:
    print(f"Caught expected error: {e}")

try:
    calculate_discount(100, 1.5)
except ValueError as e:
    print(f"Caught expected error: {e}")
