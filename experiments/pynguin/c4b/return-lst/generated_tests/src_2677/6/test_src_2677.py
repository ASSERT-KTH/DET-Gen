# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2677 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\r\x05\x15\xa4\x1e\x0br \xd8(0\xd8\x0e\x0b\x0fp\xe8\x04?\x12"
    bool_0 = False
    list_0 = [bytes_0, bool_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\r\x05\x15\xa4\x1er \xd8(0\xd8\x0e\x0b\x0fpO\x04?\x12"
    bool_0 = True
    list_0 = [bytes_0, bool_0, bytes_0]
    module_0.func(*list_0)


def test_case_3():
    int_0 = 204
    str_0 = "<cvJ~Rr&dX#Z"
    set_0 = {int_0, str_0, str_0, int_0, str_0, int_0, str_0}
    var_0 = module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -1065
    str_0 = "'.^)#\rI:&7"
    set_0 = {int_0, str_0, str_0}
    module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 198
    str_0 = "<c:\x0bJuRr&X#."
    set_0 = {int_0, str_0, str_0, str_0, str_0}
    module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = -460
    str_0 = ">Y]H"
    set_0 = {int_0, str_0, str_0, str_0, str_0}
    module_0.func(*set_0)


def test_case_7():
    int_0 = 204
    str_0 = "<c<vJ~R&dX#Z"
    set_0 = {int_0, str_0, str_0, int_0, str_0, str_0, int_0}
    var_0 = module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    int_0 = 223
    str_0 = "<cvJuRr&dX#."
    set_0 = {int_0, str_0, str_0, int_0, str_0, int_0, str_0}
    var_0 = module_0.func(*set_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_9():
    int_0 = 237
    str_0 = "<cvJuRr&dX#."
    set_0 = {int_0, str_0, str_0, int_0, str_0, int_0, str_0}
    var_0 = module_0.func(*set_0)
    module_0.func()
