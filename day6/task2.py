import pandas as pd

marks = pd.Series(
    [75, 45, 88, 60, 92],
    index=["Maths", "Physics", "Chemistry", "English", "Computer"])

print("Series:")
print(marks)

print("\nValue using position:")
print(marks.iloc[0])

print("\nValue using label:")
print(marks.loc["Chemistry"])

print("\nValues:")
print(marks.values)

print("\nIndex:")
print(marks.index)

print("\nMarks above 60:")
print(marks[marks > 60])