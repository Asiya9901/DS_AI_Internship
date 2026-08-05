print("\n welcome to Shopping Cart")
cart = []
while True:
    item = input("Enter a cart item (or type 'done' to finish): ")

    if item== "done":
        break
    cart.append(item)

print("List Type:", type(cart))
print("Total Items:", len(cart))
print("Cart Items:", cart)
cart_tuple = tuple(cart)
print("\nAfter Converting to Tuple")
print("Tuple Type:", type(cart_tuple))
print("Cart Items in Tuple:", cart_tuple)
print("CHECKOUT......")