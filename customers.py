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