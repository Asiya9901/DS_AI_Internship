import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students1.csv")

df = df.dropna(how="all")

print(df)

plt.bar(df["Name"], df["Math"])

plt.xlabel("Student")
plt.ylabel("Math Marks")
plt.title("Student Math Marks")

plt.show()