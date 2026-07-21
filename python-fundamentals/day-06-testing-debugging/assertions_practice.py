def calculate_discount(price: float, discount: float) -> float:
    """Return the price after applying a percentage discount."""
    return price - (price * discount / 100)


original_price = 100.0
final_price = calculate_discount(original_price, 20)

assert final_price == 80.0
assert final_price < original_price
assert final_price >= 0

print("All assertions passed.")