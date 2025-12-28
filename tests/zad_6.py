from logic import word_frequencies


def test_word_frequencies_1():
    assert(word_frequencies("To be or not to be"))

def test_word_frequencies_2():
    assert(word_frequencies("Hello, hello!"))

def test_word_frequencies_3():
    assert(word_frequencies(""))

def test_word_frequencies_4():
    assert(word_frequencies("Ala ma kota, a kot ma Ale."))
