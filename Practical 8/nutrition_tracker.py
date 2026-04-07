# nutrition_tracker.py
# A script to track daily nutritional intake using classes and functions

# 1. Define the food_item class
class food_item:
    # The __init__ method initializes the attributes of the object
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

# 2. Define the function to calculate total nutrition and provide warnings
def analyze_daily_nutrition(food_list):
    total_calories = 0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0

    # Iterate through the list of food_item objects to calculate totals
    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    # Print the summary
    print("--- Daily Nutritional Summary ---")
    print(f"Total Calories: {total_calories} kcal")
    print(f"Total Protein: {total_protein} g")
    print(f"Total Carbohydrates: {total_carbs} g")
    print(f"Total Fat: {total_fat} g")
    print("---------------------------------")

    # Check against recommended limits and print warnings if necessary
    if total_calories > 2500:
        print("WARNING: You have exceeded the daily limit of 2,500 calories!")
    if total_fat > 90:
        print("WARNING: You have exceeded the daily limit of 90 g of fat!")

# 3. Example of using the class and function
print("Generating nutritional report...\n")

# Create instances (objects) of the food_item class
apple = food_item("Apple", 60, 0.3, 15.0, 0.5)
burger = food_item("Cheeseburger", 850, 40.0, 50.0, 45.0)
fries = food_item("Large Fries", 500, 5.0, 65.0, 25.0)
milkshake = food_item("Chocolate Milkshake", 1200, 15.0, 150.0, 30.0)

# Store the objects in a list representing a 24-hour consumption period
daily_meals = [apple, burger, fries, milkshake]

# Call the function with the list of food items
analyze_daily_nutrition(daily_meals)