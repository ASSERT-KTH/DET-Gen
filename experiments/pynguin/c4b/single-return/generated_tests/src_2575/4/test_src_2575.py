# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2575 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "s1#YK~m)&= \r6/S4"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "56`Zs=VV8\x0cKS3,>M36%"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "@qIJ{P'%Hf]KKx\x0c`gW~"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func()
