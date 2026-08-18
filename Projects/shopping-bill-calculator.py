product1 = input("Enter product name :")
quantity1 = int(input("Enter quantity :"))
price1 = float(input("Enter Price :"))

product2 = input("Enter product name :")
quantity2 = int(input("Enter quantity :"))
price2 = float(input("Enter Price :"))

product3 = input("Enter product name :")
quantity3 = int(input("Enter quantity :"))
price3 = float(input("Enter Price :"))


total_amount =((quantity1 * price1 )+ (quantity2 * price2 ) + (quantity3 * price3 )) 
print("Total Amount ", total_amount)

if total_amount >= 5000:
    discount = total_amount * 20 / 100

elif total_amount >= 3000:
    discount = total_amount * 10 / 100

elif total_amount >= 1000:
    discount = total_amount * 5 / 100

else:
    discount = 0

print("Discount :", discount)


bill = total_amount - discount 

gst = bill * 18 / 100
print("GST :", gst)

total_bill = bill + gst
print("Total bill :", total_bill)

print("Thank you for Shopping")