# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1768 as module_0
import builtins as module_1


def test_case_0():
    str_0 = '.!ib"dP*@?}\\`%|2_9x'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.!ib"dP*@?}\\`%|2_9x'
    var_1 = module_0.func(*var_0)


def test_case_1():
    str_0 = "stD%i(@Z\rM\\U]gm0"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "stD%i(@Z\rM\\U]gm0"


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x9eZ\xab(\xf7\xf1\x9f\x87\x8f\x97ov,\x8a\x98p\xe5\xd2\xf0"
    module_0.func(*bytes_0)


def test_case_3():
    str_0 = '.!ib"dP*@?}\\`%|2_9x'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.!ib"dP*@?}\\`%|2_9x'
    var_1 = module_0.func(*list_0)
    assert var_1 == '.!ib"dP*@?}\\`%|2_9x'


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "OU#"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "ou#"
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "bWV?)"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Bwv?)"
    module_0.func()
