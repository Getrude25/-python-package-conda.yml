def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    Applies the discount only if discount_percent is 20% or higher.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

def main():
    try:
        original_price = float(input("Enter the original price: "))
        discount_pct   = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Please enter valid numbers for price and percentage.")
        return

    final_price = calculate_discount(original_price, discount_pct)

    if discount_pct >= 20:
        print(f"Discount applied! Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: {original_price:.2f}")

if __name__ == "__main__":
    main()