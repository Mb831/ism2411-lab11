# Exercise 1 - One Customer

customer = {
    "name": "Alice",
    "email": "alice@gmail.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)
# Exercise 2 - Update and Add

customer["phone"] = "555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)
# Exercise 3 - Safe Lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

# Exercise 4 - Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives the keys
for key in customer:
    print(key)

# Exercise 5 - Lookup Table

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

price = 200
final_price = price * (1 - discount)

print("Tier:", tier)
print("Discount:", f"{discount * 100}%")
print("Final Price: $", f"{final_price:.2f}")

# Exercise 6 - List of Dictionaries

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(f"{name} - {tier} - Discount: ${discount_amount:.2f}")
# Exercise 7 - Nested Catalog

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} left")