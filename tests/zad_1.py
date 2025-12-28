from logic import is_palindrome


def test_palindrome_1():
    assert is_palindrome("kajak") == True

def test_palindrome_2():
    assert is_palindrome("Kobyła ma mały bok") == True

def test_palindrome_3():
    assert is_palindrome("python") == False

def test_palindrome_4():
    assert is_palindrome("") == True

def test_palindrome_5():
    assert is_palindrome("A") == True