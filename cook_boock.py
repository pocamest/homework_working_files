def read_file(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().strip().split('\n\n')


def get_cook_book(recipes: list[str]) -> dict[str, list[dict[str, str | int]]]:
    cook_book = {}
    for recipe in recipes:
        dish, _, *ingredients = recipe.split('\n')
        cook_book[dish] = []
        for ingredient in ingredients:
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredient_dict = {
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure,
            }
            cook_book[dish].append(ingredient_dict)
    return cook_book


def get_shop_list_by_dishes(
    cook_book: dict[str, list[dict[str, str | int]]],
    dishes: list[str],
    person_count: int,
) -> dict[str, dict[str, str | int]]:
    all_ingredients = {}
    for dish in dishes:
        try:
            ingredients = cook_book[dish]
        except KeyError:
            print(f'Блюдо {dish} отсутствует в кулинарной книге')
            continue
        for ingredient in ingredients:
            name = ingredient["ingredient_name"]
            quantity = int(ingredient["quantity"])
            measure = ingredient["measure"]
            all_ingredients.setdefault(
                name,
                {'measure': measure, 'quantity': 0},
            )
            all_ingredients[name]['quantity'] += quantity * person_count
    return all_ingredients


cook_book = get_cook_book(read_file('recipes.txt'))
print(get_shop_list_by_dishes(cook_book, ['Фахитос', 'Омлет'], 2))
