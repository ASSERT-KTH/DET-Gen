# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"0\x92\xd0\x18\x1bCV\x0e\x02d6\x97"
    var_0 = module_0.flatten(bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xf1\x1bC\xfdV\x0eb"
    bool_0 = True
    str_0 = "UA=vLo]S-p"
    list_0 = [bytes_0, str_0, bool_0, bool_0]
    tuple_0 = (bool_0, bool_0, list_0)
    var_0 = module_0.flatten(tuple_0)
    module_1.object(*var_0)