def count_vowels(text: str) -> int:

    vowels = set("aeiouyąęó")

    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


print(count_vowels("Python"))
print(count_vowels("AEIOUY"))
print(count_vowels("bcd"))
print(count_vowels(""))
print(count_vowels("Próba żółwia"))
