# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2677 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "&;7!|*2:\t?OS"
    bool_0 = True
    list_0 = [str_0, bool_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "&;!|9*2:\t?OS"
    bool_0 = False
    list_0 = [str_0, bool_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\r%>f["
    bool_0 = False
    list_0 = [str_0, bool_0, bool_0]
    module_0.func(*list_0)


def test_case_4():
    str_0 = "^P<"
    bool_0 = False
    list_0 = [str_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "^P<"
    bool_0 = True
    list_0 = [str_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "vU/hfKnRtb6v"
    bool_0 = False
    list_0 = [str_0, bool_0, bool_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "<P<"
    bool_0 = False
    list_0 = [str_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
