# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import src_2054 as module_0


def test_case_0():
    bytes_0 = b"\xab\xd8s\x17m\xe7\x9aa\xf0L&\x01\x82\xf2\xa9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 99


def test_case_1():
    bool_0 = False
    bool_1 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_1: bool_0, bool_1: bool_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 0
