def calculate_discount(price, discount_percent):
    # Apply discount only if it's 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(original_price, discount)

# Print result
print(f"The final price is: {final_price}")
