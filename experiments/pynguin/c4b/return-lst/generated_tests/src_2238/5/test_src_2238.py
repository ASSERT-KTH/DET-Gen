# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2238 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b':O\x1d\x1e\x9e\xd4\xa0\xb50\x1b\xd6\x14h"i\x97e\x1d\xbb\xf4'
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "D\x0chnf/,Ff9:.MiX"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_0.func()