# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1960 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"N.\x9a"
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "2 4 7 11 16 22 29 37 46 56 67 1 14 28 43 59 76 16 35 55 76 20 43 67 14 40 67 17 46 76 29 61 16 50 7 43 2 40 1 41 4 46 11 55 22 68 37 7 56 28 1 53 28 4 59 37 16 74 55 37 20 4 67 53 40 28 17 7 76 68 61 55 50 46 43 41 40"
    )
#    module_0.func()
