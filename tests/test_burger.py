import unittest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger(unittest.TestCase):

    def test_set_bun_successfully(self):
        mock_bun = Bun('Флюоресцентная булка R2-D3', 988)
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.get_name() == 'Флюоресцентная булка R2-D3', 'Булочка не установлена'

    def test_add_ingredient_successfully(self):
        mock_ingredient = Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients, 'Ингредиент не добавлен'

    def test_remove_ingredient_successfully(self):
        mock_ingredient1 = Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)
        mock_ingredient2 = Ingredient('Соус', 'Соус Spicy-X', 90)
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(0)
        assert mock_ingredient1 not in burger.ingredients, 'Ингредиент не удалён'
        assert mock_ingredient2 in burger.ingredients, 'Ингредиент 2 не должен уйти'

    def test_move_ingredient_success(self):
        mock_ingredient1 = Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)
        mock_ingredient2 = Ingredient('Соус', 'Соус Spicy-X', 90)
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == mock_ingredient2, 'Ингредиенты не перемещены правильно'
        assert burger.ingredients[1] == mock_ingredient1, 'Ингредиенты не перемещены правильно'

    def test_get_price_without_ingredients(self):
        mock_bun = Bun('Флюоресцентная булка R2-D3', 988)
        burger = Burger()
        burger.set_buns(mock_bun)
        price = burger.get_price()
        expected_price = 988 * 2

        assert price == expected_price, 'Цена рассчитана неправильно'

    def test_get_price_with_ingredients(self):
        mock_bun = Bun('Флюоресцентная булка R2-D3', 988)
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_ingredient1 = Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)
        mock_ingredient2 = Ingredient('Соус', 'Соус Spicy-X', 90)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        price = burger.get_price()
        expected_price = 988 * 2 + 3000 + 90

        assert price == expected_price, 'Цена рассчитана неправильно с ингредиентами'

    def test_get_receipt(self):
        mock_bun = Bun('Флюоресцентная булка R2-D3', 988)
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_ingredient = Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        expected_receipt = (
            '(==== Флюоресцентная булка R2-D3 ====)\n'
            '= начинка Говяжий метеорит (отбивная) =\n'
            '(==== Флюоресцентная булка R2-D3 ====)\n'
            '\n'
            'Price: 4976'
        )

        print("Receipt:")
        print(receipt.strip())
        print("Expected Receipt:")
        print(expected_receipt.strip())

        assert receipt.strip() == expected_receipt.strip(), 'Чек сформирован неправильно'
