#Sale analysis

sales = [
    {"name": "Apple", "cost": 1.2, "quantity": 17},
    {"name": "Banana", "cost": 0.8, "quantity": 25},
    {"name": "Orange", "cost": 1.5, "quantity": 4},
    {"name": "Milk", "cost": 2.3, "quantity": 5},
    {"name": "Bread", "cost": 1.7, "quantity": 2}
]

top_product = None
qty = 0
print("Best sales: ")
for sale in sales:
    if sale['quantity'] >=5 and sale['quantity'] * sale['cost'] >= 20:
        print(f"{sale['name']} - {sale['cost'] * sale['quantity']}$")
        if sale["quantity"] > qty:
            top_product = sale["name"]
            qty = sale['quantity']
        

print(f"Top product - {top_product} - {qty}")