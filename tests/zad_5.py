from logic import flatten_list

def test_flatten_list_1():
    assert(flatten_list([1, 2, 3]))

def test_flatten_list_2():
    assert(flatten_list([1, [2, 3], [4, [5]]]))

def test_flatten_list_3():
    assert(flatten_list([]))

def test_flatten_list_4():
    assert(flatten_list([[[1]]]))

def test_flatten_list_5():
    assert(flatten_list([1, [2, [3, [4]]]]))
