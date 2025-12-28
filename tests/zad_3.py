from logic import count_vowels


def test_count_vowels_1():
    assert(count_vowels("Python"))

def test_count_vowels_2():
    assert (count_vowels("AEIOUY"))

def test_count_vowels_3():
    assert (count_vowels("bcd"))

def test_count_vowels_4():
    assert (count_vowels(""))

def test_count_vowels_5():
    assert (count_vowels("Próba żółwia"))
