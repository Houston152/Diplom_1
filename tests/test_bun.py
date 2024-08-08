import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name, price", [
    ("Флюоресцентная булка R2-D3", 988.0),
    ("Краторная булка N-200i", 1255.0)
])
def test_bun_initialization(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price


def test_bun_get_name():
    bun = Bun("Флюоресцентная булка R2-D3", 988.0)
    assert bun.get_name() == "Флюоресцентная булка R2-D3"


def test_bun_get_price():
    bun = Bun("Краторная булка N-200i", 1255.0)
    assert bun.get_price() == 1255.0
