# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_954 as module_0


def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ""


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x0e\x8aF\x88\xf9\x01\xf1\xc0\xd6\x08/\x1f\xd6\xa4\xb7\xa7\xaa"
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love that I hate that I love it"
    )
#    module_0.func()
