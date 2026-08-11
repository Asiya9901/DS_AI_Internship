import pandas as pd

names = pd.Series([
    "ASiya",
    "Ash",
    None,
    "harini",
    "wnu",
    None
])

print("Original Series:")
print(names)


print("\nMissing values:")
print(names.isna())


names = names.fillna("Unknown")

print("\nAfter filling missing values:")
print(names)


names = names.str.lower()

print("\nLowercase names:")
print(names)


result = names[names.str.contains("a")]

print("\nNames containing 'a':")
print(result)