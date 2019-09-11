# content of test_sample.py
def inc(x):
    return x + 1

def int_num(f):
    return int(f)

def test_answer():
    assert inc(4) == 5, "Adds up"
    assert int_num(3.1) == 3, "compared"