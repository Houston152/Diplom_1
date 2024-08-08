from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_database_initialization():
    db = Database()
    assert len(db.available_buns()) == 3
    assert len(db.available_ingredients()) == 6


def test_available_buns():
    db = Database()
    buns = db.available_buns()
    assert buns[0].get_name() == "black bun"
    assert buns[1].get_name() == "white bun"
    assert buns[2].get_name() == "red bun"


def test_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()

    assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[1].get_name() == "sour cream"
    assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
    assert ingredients[3].get_name() == "cutlet"
