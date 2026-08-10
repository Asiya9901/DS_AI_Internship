import random

print("Random:", random.random())
print("Random Integer:", random.randint(1, 10))
print("Random Float:", random.uniform(1, 10))
print("Random Choice:", random.choice(["Apple", "Mango", "Banana"]))
print("Random Range:", random.randrange(1, 10))

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)
print("Shuffle:", numbers)

print("Sample:", random.sample([1, 2, 3, 4, 5], 2))
print("Choices:", random.choices([1, 2, 3, 4, 5], k=3))

random.seed(10)
print("Seed:", random.random())