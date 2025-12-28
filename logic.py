def is_palindrome(text: str) -> bool:

    clean_text = "".join(text.split()).casefold()

    return clean_text == clean_text[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Index cannot be negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def count_vowels(text: str) -> int:

    vowels = set("aeiouyąęó")

    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


def calculate_discount(price: float, discount: float) -> float:

    if not (0.0 <= discount <= 1.0):
        raise ValueError("Discount must be between 0 and 1 (inclusive).")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    final_price = price * (1 - discount)

    return float(final_price)


def flatten_list(nested_list: list) -> list:

    flat_list = []

    for item in nested_list:

        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)

    return flat_list



import re
from collections import Counter


def word_frequencies(text: str) -> dict:

    text_lower = text.lower()

    words = re.findall(r'\w+', text_lower)

    counts = Counter(words)

    return dict(counts)


import math


def is_prime(n: int) -> bool:

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1

    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True