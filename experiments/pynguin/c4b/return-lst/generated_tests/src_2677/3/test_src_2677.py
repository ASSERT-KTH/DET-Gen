# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2677 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    list_0 = [tuple_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    list_0 = [tuple_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "#~>aAh#6_TKd+"
    float_0 = 2341.865312189898
    set_0 = {str_0, float_0}
    module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "<:bE,!4NqgOKu\\(#KlD"
    float_0 = 2357.1833565340844
    set_0 = {str_0, float_0}
    module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "<:bE,!4NqgOKu\\(#KlD"
    float_0 = 2355.239930570657
    list_0 = [str_0, float_0, float_0, str_0]
    module_0.func(*list_0)


def test_case_6():
    str_0 = ">~>aAh#6_Tsd+"
    float_0 = 2341.865312189898
    set_0 = {str_0, float_0}
    var_0 = module_0.func(*set_0)


def test_case_7():
    str_0 = ">~>aAh#6d_Tsd+"
    float_0 = 2324.1617880905105
    set_0 = {str_0, float_0, float_0, str_0}
    var_0 = module_0.func(*set_0)


def test_case_8():
    str_0 = "vH>E<C3OT]T>"
    float_0 = 2341.865312189898
    set_0 = {str_0, float_0}
    var_0 = module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "^]Z]Oeh:d*wkS8\n/I3h<"
    float_0 = -1811.97
    set_0 = {float_0, str_0, str_0}
    module_0.func(*set_0)


def test_case_10():
    str_0 = ">A<aKh>_T:d+"
    float_0 = -746.2363700884308
    set_0 = {float_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
