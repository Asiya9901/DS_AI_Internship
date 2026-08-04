string=input("enter the string")

rev=string[::-1]
if string==rev:
    print("palindrome")
else:
    print("not palindrome")