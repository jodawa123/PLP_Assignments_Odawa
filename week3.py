def calculate_discount(price,discount_percent):
    if discount_percent >= 0.2:
        new_price= price - (discount_percent * price)
        return new_price
    else:
        return price
            

a= float(input("Enter the original price: "))
b= float(input("Enter the the discount precentage: "))
b=b/100
final_price=calculate_discount(a,b)
print("Final price after discount is: ",final_price)
