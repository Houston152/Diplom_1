import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0),
    (INGREDIENT_TYPE_FILLING, "Хрустящие минеральные кольца", 300.0),
])
def test_ingredient_initialization(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type  # Проверяем тип
    assert ingredient.get_name() == name            # Проверяем имя
    assert ingredient.get_price() == price          # Проверяем цену


def test_get_name():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Хрустящие минеральные кольца", 300.0)
    assert ingredient.get_name() == "Хрустящие минеральные кольца"


def test_get_price():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0)
    assert ingredient.get_price() == 90.0


def test_get_type():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Хрустящие минеральные кольца", 300.0)
    assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
