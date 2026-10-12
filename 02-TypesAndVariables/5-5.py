price = float(input("price: "))
discount = float(input("discount in %"))

price_with_discount = price*(100-discount)/100
reduction = price - price_with_discount

print(f"Price {round(price,2)}")
print(f"Discount {round(discount,2)}")
print(f"Price with discount {round(price_with_discount,2)}")
print(f"Reduction {round(reduction,2)}")
