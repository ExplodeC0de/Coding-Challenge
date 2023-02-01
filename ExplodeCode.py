# Shop Checkout System

# Create an empty cart list to store the items
cart = []

# Create a dictionary to store the item prices
prices = {
    "pasta": 4.00,
    "pizza": 5.00,
    "cookies": 3.00,
    "rice": 1.00,
    "milk": 0.50,
    "banana": 0.75,
    "bread": 2.00,
    "cheese": 3.00,
    "juice": 2.50,
    "sugar": 2.00,
    "salt": 1.00,
    "pepper": 0.50,
    "flour": 1.50,
    "baking_powder": 0.75,
    "vanilla_extract": 3.00,
    "chocolate_chips": 2.00,
    "cocoa_powder": 2.50,
    "butter": 3.00,
    "oil": 2.00,
    "mayonnaise": 2.50,
    "mustard": 1.50,
    "ketchup": 2.00,
    "hot_sauce": 2.00,
    "soy_sauce": 2.00,
    "teriyaki_sauce": 2.50,
    "vinegar": 1.50,
    "worcestershire_sauce": 2.00,
    "bbq_sauce": 2.50,
    "canned_tomatoes": 1.50,
    "diced_tomatoes": 1.75,
    "tomato_sauce": 1.50,
    "tomato_paste": 1.50,
    "crushed_tomatoes": 1.75,
    "spaghetti_sauce": 2.50,
    "macaroni": 1.50,
    "beans": 1.50,
    "lentils": 2.00,
    "chickpeas": 1.75,
    "peas": 1.50,
    "corn": 1.75,
    "carrots": 0.75,
    "potatoes": 1.00,
    "onions": 0.75,
    "garlic": 0.50,
    "ginger": 1.00,
    "lemons": 0.50,
    "limes": 0.50

}

# Create a function to add items to the cart
def add_item():
    item = input("Enter the item name: ")
    if item in prices:
        cart.append(item)
        print(f"{item} added to cart.")
    else:
        print("Item not found.")

# Create a function to show the items in the cart and the total price
def checkout():
    total = 0
    print("Items in cart:")
    for item in cart:
        print(f"- {item}: £{prices[item]}")
        total += prices[item]
    print(f"Total: £{total}0")

# Call the add_item function multiple times to allow the shopper to input items
while True:
    add_item()
    another = input("Add another item? (y/n): ")
    if another.lower() == "n":
        break

# Call the checkout function to show the items and total price
checkout()
