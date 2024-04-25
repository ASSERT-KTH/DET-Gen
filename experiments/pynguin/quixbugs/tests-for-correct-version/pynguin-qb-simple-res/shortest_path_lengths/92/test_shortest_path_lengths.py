# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_lengths as module_0
import collections as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.shortest_path_lengths(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -2873
    module_0.shortest_path_lengths(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.shortest_path_lengths(none_type_0, none_type_0)


def test_case_3():
    dict_0 = {}
    bool_0 = False
    var_0 = module_0.shortest_path_lengths(bool_0, dict_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(var_0) == 0
    assert (
        f"{type(module_1.defaultdict.default_factory).__module__}.{type(module_1.defaultdict.default_factory).__qualname__}"
        == "builtins.member_descriptor"
    )


@pytest.mark.xfail(strict=True)
def test_case_4():
    dict_0 = {}
    bool_0 = True
    var_0 = module_0.shortest_path_lengths(bool_0, dict_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(var_0) == 1
    assert (
        f"{type(module_1.defaultdict.default_factory).__module__}.{type(module_1.defaultdict.default_factory).__qualname__}"
        == "builtins.member_descriptor"
    )
    bool_1 = False
    var_1 = module_0.shortest_path_lengths(bool_1, dict_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(var_1) == 0
    module_0.shortest_path_lengths(bool_1, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 31
    list_0 = []
    var_0 = module_0.shortest_path_lengths(int_0, list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(var_0) == 961
    assert (
        f"{type(module_1.defaultdict.default_factory).__module__}.{type(module_1.defaultdict.default_factory).__qualname__}"
        == "builtins.member_descriptor"
    )
    bytes_0 = b"\xbdq\xea\xebA\xaeym\xce\xa06\xd2IV\x1bB\xeaJ"
    module_0.shortest_path_lengths(bytes_0, bytes_0)