def read_file(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().strip().split('\n\n')


def making_cookbook(recipes: list[str]) -> dict[str, list[dict[str, str]]]:
    cook_book = {}
    for recipe in recipes:
        cook_book.update(formating_recipe(recipe))
    return cook_book


def formating_recipe(recipe: str) -> dict[str, list[dict[str, str]]]:
    dish, _, *ingredients = recipe.split('\n')
    ingredients_list = [formating_ingredient(ingredient)
                        for ingredient in ingredients]
    return {dish: ingredients_list}


def formating_ingredient(ingredient: str) -> dict[str, str]:
    keys_ingredient = ['ingredient_name', 'quantity', 'measure']
    return dict(zip(keys_ingredient, ingredient.split(' | ')))


print(making_cookbook(read_file('recipes.txt')))
