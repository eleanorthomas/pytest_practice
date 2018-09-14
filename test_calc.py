from calc import add_numbers

def test_add_numbers_1_2():
    assert(add_numbers(1, 2) == 3)

def test_add_numbers_5_7():
    assert(add_numbers(5, 7) == 12)

def test_add_numbers_0_4():
    assert(add_numbers(0, 4) == 4)

def test_add_numbers_neg1_1():
    assert(add_numbers(-1, 1) == 0)
