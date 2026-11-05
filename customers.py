# customers.py
# Name: Jimmy Reyes
# ISM2411 — Module 11 Lab
# Self Assessment Qs
# 1. In real work, I would use brackets when a customer ID or an order total is supposed to be there. I would use .get() when the key is optional or sometimes missing, for example, a phone number, middle name, or a coupon code. if the data missing means and error, then use brackets. If data missing is normal and is not an error, I would use .get().
# 2. In Excel, it reminds me of a PivotTable, grouping rows by category and counting them. Python can be more useful with big data because it is repeatable, can handle larger data sets, it is automatable, and it makes fewer mistakes a human can make.

print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2
print("--- Exercise 2 ---")
customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print(customer.get("email", "Email not found"))

print("--- Exercise 3 ---")

#New Version
print(customer.get("email", "no email on file"))

#Older version
# try:
#     print(customer["email"])
# except KeyError as error:
#     print(f"KeyError Caught: {error}")

print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key} : {value}")

for item in customer:
    print(item)

print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0,
                  "silver" : 0.05,
                  "gold": 0.10,
                  "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}") # platinum
print(f"Discount; {discount_rate * 100:.0f}%") # 15%
print(f"Final price: ${final_price:.2f}") # $170.00

print("--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")

print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")

print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}): {sales_by_region[region]}")