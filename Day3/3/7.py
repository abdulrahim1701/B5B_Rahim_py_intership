inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}


def add_stock(product, quantity):
    inventory[product] = inventory.get(product, 0) + quantity
    print(quantity, product, "added to inventory.")


def sell_product(product, quantity):
    if product not in inventory:
        print("Error:", product, "does not exist in inventory.")
    elif inventory[product] < quantity:
        print("Error: Not enough stock of", product)
    else:
        inventory[product] -= quantity
        print(quantity, product, "sold successfully.")


add_stock("Laptop", 5)

add_stock("Monitor", 8)

sell_product("Mouse", 3)

sell_product("Printer", 2)


sell_product("Keyboard", 20)

print("\nFinal inventory:")
print(inventory)