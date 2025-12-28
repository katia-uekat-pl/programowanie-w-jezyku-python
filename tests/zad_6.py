import re
from collections import Counter


def word_frequencies(text: str) -> dict:

    text_lower = text.lower()

    words = re.findall(r'\w+', text_lower)

    counts = Counter(words)

    return dict(counts)

print(word_frequencies("To be or not to be"))
print(word_frequencies("Hello, hello!"))
print(word_frequencies(""))
print(word_frequencies("Ala ma kota, a kot ma Ale."))
