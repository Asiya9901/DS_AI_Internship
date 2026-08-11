import numpy as np

sales = np.array([
    [100, 200, 150],
    [120, 180, 170],
    [90, 220, 160],
    [110, 190, 180]
])

print("Sales Data:")
print(sales)

print("\n--- Product-wise (axis=0) ---")
print("Mean:", np.mean(sales, axis=0))
print("Median:", np.median(sales, axis=0))
print("Variance:", np.var(sales, axis=0))
print("Standard Deviation:", np.std(sales, axis=0))

print("\n--- Day-wise (axis=1) ---")
print("Mean:", np.mean(sales, axis=1))
print("Median:", np.median(sales, axis=1))
print("Variance:", np.var(sales, axis=1))
print("Standard Deviation:", np.std(sales, axis=1))