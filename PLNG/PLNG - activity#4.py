print("Input price of product#1: ")
prod1 = float(input())
print("Input price of product#2: ")
prod2 = float(input())

total = prod1 + prod2

print(f"Total price will be: {total}")

print("Please enter payment amount: ")
pay = float(input())

owed = total - pay
if pay < total:
    print(f"Your purchase is UNSUCCESSFUL! You still owe: {owed} dollars.")
else:
    print(f"Your purchase is SUCCESSFUL! Your change is: {abs(owed)}")
