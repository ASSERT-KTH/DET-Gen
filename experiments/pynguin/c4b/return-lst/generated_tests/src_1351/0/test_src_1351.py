# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1351 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    complex_0 = 3085.535368 - 189.17j
    bytes_0 = b"\x04/\xe2"
    tuple_0 = (complex_0, bytes_0)
    list_0 = [tuple_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    str_0 = ";F Aw LI;#y$a^orqla7"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    str_0 = ";F A> LI;#y$a^orqla7"
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "9c9 2Qlx5<JpIf7]]"
    str_1 = ".NJ Ik:ioJ.~*^4\x0cofn"
    bytes_0 = b"\x0ew\xd2$\xfd\xba\x02K\x93\x1f\xa5Ff\x1e\x9f\x96\xa4\x0c"
    set_0 = {bytes_0, str_1}
    tuple_0 = (str_0, str_1, set_0)
    bool_0 = False
    list_0 = [tuple_0, str_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0]
    object_0 = module_1.object()
    var_0 = module_0.func(*list_0)
    object_1 = module_1.object()
    var_1 = module_0.func(*list_0)
    str_0 = "OY=v u #G%ou}bY}"
    var_2 = module_0.func(*var_1)
    var_3 = module_0.func(*str_0)
    module_1.object(**var_1)