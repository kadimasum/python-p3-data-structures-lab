spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food.get("name") for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level") > 5]

def print_spicy_foods(spicy_foods):
    result = ""
    for food in spicy_foods:
        modified_heat_level = int(food.get("heat_level")) * "🌶"
        food["heat_level"] = modified_heat_level
        result += food.get("name") + f" ({food.get('cuisine')})" + " | Heat Level: " + modified_heat_level + "\n"
    return result


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass


print(print_spicy_foods(spicy_foods))