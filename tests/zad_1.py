import unittest

def is_palindrome(text: str) -> bool:

    clean_text = "".join(text.split()).casefold()

    return clean_text == clean_text[::-1]

test_cases = [
    ("kajak", True),
    ("Kobyła ma mały bok", True),
    ("python", False),
    ("", True),
    ("A", True)
]

for text, expected in test_cases:
    result = is_palindrome(text)
    assert result == expected, f"Błąd dla: '{text}'. Oczekiwano {expected}, otrzymano {result}"
    print(f"Test zaliczony: '{text}' -> {result}")