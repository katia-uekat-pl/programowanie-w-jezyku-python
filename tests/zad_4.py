from logic import calculate_discount


def calculate_discount_1():
    assert(calculate_discount(100, 0.2))

def test_count_vowels_2():
    assert(calculate_discount(50, 0))

def test_count_vowels_1():
    assert(calculate_discount(200, 1))

try:
    calculate_discount(100, -0.1)
except ValueError as e:
    print(f"Caught expected error: {e}")

try:
    calculate_discount(100, 1.5)
except ValueError as e:
    print(f"Caught expected error: {e}")
