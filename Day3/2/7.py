def make_frozenset(items):
    return frozenset(items)


data = [1, 2, 3, 2, 1]

result = make_frozenset(data)

print("\nFrozenset:", result)