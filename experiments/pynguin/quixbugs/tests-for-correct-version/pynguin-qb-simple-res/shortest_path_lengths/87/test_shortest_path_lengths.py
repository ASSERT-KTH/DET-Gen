# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_lengths as module_0
import collections as module_1
import builtins as module_2


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 328
    module_0.shortest_path_lengths(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.shortest_path_lengths(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    dict_0 = {}
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
    var_0.successor()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    dict_0 = {}
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
    object_0 = module_2.object()
    float_0 = 3588.196064582388
    module_0.shortest_path_lengths(float_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    dict_0 = {}
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
    int_0 = 15
    var_1 = module_0.shortest_path_lengths(int_0, dict_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(var_1) == 225
    var_2 = module_0.shortest_path_lengths(bool_0, var_0)
    assert (
        f"{type(var_2).__module__}.{type(var_2).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(var_2) == 0
    var_0.successor()