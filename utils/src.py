import requests

def get_food_info(product_name):
    url = f"https://world.openfoodfacts.org/cgi/search.pl?action=process&search_terms={product_name}&json=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        products = data.get('products', [])
        if products:  # Проверяем, есть ли найденные продукты
            first_product = products[0]
            return {
                'name': first_product.get('product_name', 'Неизвестно'),
                'calories': first_product.get('nutriments', {}).get('energy-kcal_100g', 0)
            }
        return None
    print(f"Ошибка: {response.status_code}")
    return None

workout_calories_per_min = {
    "running": 11,
    "swimming": 10,
    "yoga": 4,
    "cycling": 8,
    "weightlifting": 6,
    "hiit": 13,
    "pilates": 5,
    "rowing": 12,
    "jump_rope": 14,
    "dancing": 7,
    "fitness": 8,
    "ice_hockey": 12,
    "figure_skating": 9,
    "football": 10,
    "biathlon": 13,
    "skiing": 11,
    "boxing": 12,
    "basketball": 9,
    "auto_racing": 6,
    "athletics": 10,
    "alpine_skiing": 10,
    "volleyball": 7,
    "chess": 1,
    "wrestling": 11,
    "billiards": 2,
    "gymnastics": 8,
    "hiking": 7,
}

def get_weather():
    pass