product = ("Laptop", 75000, 5)

print("\nOriginal product:", product)

# Tuples are immutable, so this causes a TypeError:
# product[1] = 70000

# Correct way: create a new tuple
product = (product[0], 70000, product[2])

print("Updated product:", product)
