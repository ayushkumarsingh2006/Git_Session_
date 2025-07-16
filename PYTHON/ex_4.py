#AYUSH KUMAR SINGH
#USN 2102408006

#wap to calculate the final price after a discount...

total_amount = float(input("enter the amount:"))

if total_amount<1000:
    discount = 0
elif  1000<= total_amount <= 5000:
    discount = total_amount*(10/100)
else:
    discount = total_amount*(20/100)

final_price = total_amount-discount

print("the final price is:",final_price)
