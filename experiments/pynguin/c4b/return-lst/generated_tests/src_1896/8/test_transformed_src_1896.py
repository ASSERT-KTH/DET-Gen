# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1896 as module_0


def test_case_0():
    str_0 = "WphsH\\edh\x0bgLK7\x0c "
    bytes_0 = b"DE\xe4\xbb\x00\x05g>1\xf1\xa8sd\x1c\xc9\xb5\xfd/5F"
    list_0 = [str_0, str_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "WphsH\\edh\x0bgLK7\x0c "
    var_0 = module_0.func(*str_0)
#    module_0.func()
