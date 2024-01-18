def apply_discount(cart, product_prices):
    discounts = []

    if cart["total"] > 200:
        discounts.append(("flat_10_discount", 10))

    for product, quantity in cart["quantities"].items():
        if quantity > 10:
            discounts.append(("bulk_5_discount", product_prices[product] * 0.05))

    if cart["total_quantity"] > 20:
        discounts.append(("bulk_10_discount", cart["total"] * 0.1))

    if cart["total_quantity"] > 30:
        for product, quantity in cart["quantities"].items():
            if quantity > 15:
                discounts.append(("tiered_50_discount", product_prices[product] * 0.5 * (quantity - 15)))

    if discounts:
        name, amount = max(discounts, key=lambda x: x[1])
        cart["total"] -= amount
        return name, amount
    else:
        return None, 0


def calculate_shipping_and_gift_fee(cart):
    shipping_fee = (cart["total_quantity"] // 10) * 5
   
    gift_wrap_fee = sum(cart["gift_wraps"].values())
    return shipping_fee, gift_wrap_fee


def main():
    products_prices = {
        "Product A": 20,
        "Product B": 40,
        "Product C": 50,
    }

    cart = {"quantities": {}, "prices": products_prices, "total": 0, "total_quantity": 0, "gift_wraps": {}}

    for product, price in products_prices.items():
        quantity = int(input(f"Enter quantity for {product}: "))
        is_gift_wrapped = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"
        cart["gift_wraps"][product] = 1 if is_gift_wrapped else 0
        cart["quantities"][product] = quantity
        cart["total"] += quantity * price + cart["gift_wraps"][product]
        cart["total_quantity"] += quantity

    discount_name, discount_amount = apply_discount(cart, products_prices)
    
    shipping_fee, gift_wrap_fee = calculate_shipping_and_gift_fee(cart)

    print("\nOrder Summary:")
    for product, quantity in cart["quantities"].items():
        print(f"{product}: {quantity} units - ${quantity * products_prices[product]}")

    print("\nSubtotal:", cart["total"])
    print("Discount Applied:", discount_name, "-", discount_amount)
    print("Shipping Fee:", shipping_fee)
    print("Gift Wrap Fee:", gift_wrap_fee)
    print("Total:", cart["total"] + shipping_fee + gift_wrap_fee)


if __name__ == "__main__":
    main()
