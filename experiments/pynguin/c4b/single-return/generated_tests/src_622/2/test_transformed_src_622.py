# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_622 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"V\x97<\x12\x97\xe9}\xa2xR\xbc\xeb"
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "86 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85"
    )
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    int_0 = 396
    set_0 = {bool_0, int_0, int_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "0"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
#    module_0.func(*list_0)
