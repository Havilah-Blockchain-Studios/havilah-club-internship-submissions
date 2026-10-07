import requests

BASE_URL = "https://world.openfoodfacts.org/api/v2/search"


def fetch_data(category):
    params = {
        "categories_tags": category,
        "fields": "product_name,brands,nutriscore_grade",
        "page_size": 5,
    }
    headers = {"User-Agent": "HavilahDay14FoodApp/1.0 (student project)"}

    try:
        response = requests.get(BASE_URL, params=params, headers=headers, timeout=10)
    except requests.exceptions.RequestException as error:
        print("Network problem, could not reach the API:", error)
        return None

    print("Status code:", response.status_code)
    print("Request URL:", response.url)

    if response.status_code == 200:
        return response.json()
    else:
        print("The API returned an error. Status code:", response.status_code)
        return None


def display_results(data, category):
    print()
    print("=" * 40)
    print("Food products in category:", category)
    print("Total products found:", data["count"])
    print("Showing:", len(data["products"]))
    print("=" * 40)
    print()

    if len(data["products"]) == 0:
        print("No products found. Try a category like 'biscuits'.")
        return

    number = 1
    for product in data["products"]:
        name = product.get("product_name", "Unknown")
        brand = product.get("brands", "Unknown")
        grade = product.get("nutriscore_grade", "Unknown")

        print(str(number) + ". " + name)
        print("   Brand:", brand)
        print("   Nutri-Score:", grade.upper())
        print("-" * 40)

        number = number + 1


def main():
    category = input("Enter a food category (e.g. breakfast-cereals): ")
    data = fetch_data(category)
    if data:
        display_results(data, category)


if __name__ == "__main__":
    main()