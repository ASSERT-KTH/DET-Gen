# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2113 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xf4\xaf\xb5Ei\xcbv\xd9J:\x15\xf6Jd\x14\xe6"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "IL\\H)"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"(\xc2>\xf0\xa0\xdc\xa1\xc4Z\xdbav\x1e\xf9"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x91\x043\x16\x0ca\xf6:z\xa2~\xa64\xb1"
    var_0 = module_0.func(*bytes_0)
    module_1.object(*var_0)