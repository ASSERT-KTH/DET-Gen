# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1295 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"-\x87(iV\xbc\xe7\x8e\xadw"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    var_1 = module_0.func(*list_0)
    assert var_1 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "t.[d`9{y+.vFM"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ");1;aw`Hw>sR"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ");aw`Q>sRm"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    none_type_0 = None
    module_0.func(*none_type_0)
