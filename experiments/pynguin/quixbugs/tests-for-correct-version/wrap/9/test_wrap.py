# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    module_0.wrap(none_type_0, none_type_0)


def test_case_1():
    bool_0 = True
    str_0 = "\nuq5!f8O=k"
    var_0 = module_0.wrap(str_0, bool_0)


def test_case_2():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    var_0 = module_0.wrap(set_0, bool_0)
    var_1 = module_0.wrap(set_0, bool_0)
