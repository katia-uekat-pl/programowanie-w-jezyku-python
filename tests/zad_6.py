from logic import word_frequencies


def test_word_frequencies_1():
    assert word_frequencies("To be or not to be") == {"to": 2, "be": 2, "or": 1, "not": 1}

def test_word_frequencies_2():
    assert word_frequencies("Hello, hello!") == {"hello": 2}

def test_word_frequencies_3():
    assert word_frequencies("") =={}

def test_word_frequencies_4():
    assert word_frequencies("Python Python python") == {"python": 3}

def test_word_frequencies_5():
    assert word_frequencies("Ala ma kota, a kot ma Ale.") == {'a': 1, 'ala': 1, 'ale': 1, 'kot': 1, 'kota': 1, 'ma': 2}
