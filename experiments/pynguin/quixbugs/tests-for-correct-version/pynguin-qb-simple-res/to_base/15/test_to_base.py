# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0
import re as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    none_type_0 = None
    module_0.to_base(bool_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    none_type_0 = None
    var_0 = module_0.to_base(bool_0, none_type_0)
    assert var_0 == ""
    var_1 = module_0.to_base(bool_0, bool_0)
    assert var_1 == ""
    var_2 = module_1.fullmatch(var_1, var_0)
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "re.Match"
    assert module_1.ASCII == module_1.RegexFlag.ASCII
    assert module_1.A == module_1.RegexFlag.ASCII
    assert module_1.IGNORECASE == module_1.RegexFlag.IGNORECASE
    assert module_1.I == module_1.RegexFlag.IGNORECASE
    assert module_1.LOCALE == module_1.RegexFlag.LOCALE
    assert module_1.L == module_1.RegexFlag.LOCALE
    assert module_1.UNICODE == module_1.RegexFlag.UNICODE
    assert module_1.U == module_1.RegexFlag.UNICODE
    assert module_1.MULTILINE == module_1.RegexFlag.MULTILINE
    assert module_1.M == module_1.RegexFlag.MULTILINE
    assert module_1.DOTALL == module_1.RegexFlag.DOTALL
    assert module_1.S == module_1.RegexFlag.DOTALL
    assert module_1.VERBOSE == module_1.RegexFlag.VERBOSE
    assert module_1.X == module_1.RegexFlag.VERBOSE
    assert module_1.TEMPLATE == module_1.RegexFlag.TEMPLATE
    assert module_1.T == module_1.RegexFlag.TEMPLATE
    assert module_1.DEBUG == module_1.RegexFlag.DEBUG
    assert (
        f"{type(module_1.Match.string).__module__}.{type(module_1.Match.string).__qualname__}"
        == "builtins.member_descriptor"
    )
    assert (
        f"{type(module_1.Match.re).__module__}.{type(module_1.Match.re).__qualname__}"
        == "builtins.member_descriptor"
    )
    assert (
        f"{type(module_1.Match.pos).__module__}.{type(module_1.Match.pos).__qualname__}"
        == "builtins.member_descriptor"
    )
    assert (
        f"{type(module_1.Match.endpos).__module__}.{type(module_1.Match.endpos).__qualname__}"
        == "builtins.member_descriptor"
    )
    assert (
        f"{type(module_1.Match.lastindex).__module__}.{type(module_1.Match.lastindex).__qualname__}"
        == "builtins.getset_descriptor"
    )
    assert (
        f"{type(module_1.Match.lastgroup).__module__}.{type(module_1.Match.lastgroup).__qualname__}"
        == "builtins.getset_descriptor"
    )
    assert (
        f"{type(module_1.Match.regs).__module__}.{type(module_1.Match.regs).__qualname__}"
        == "builtins.getset_descriptor"
    )
    module_0.to_base(var_2, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 549
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    module_0.to_base(var_0, var_0)