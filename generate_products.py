import random

categories = {
    1: 'Electronics',
    2: 'Books',
    3: 'Clothing',
    4: 'Home Appliances',
    5: 'Fitness',
    6: 'Footwear',
    7: 'Toys',
    8: 'Groceries'
}

num_products = 50

with open('insert_products.sql', 'w') as f:
    for product_id in range(1, num_products + 1):
        name = f"Product{product_id}"
        category_id = random.randint(1, len(categories))
        price = round(random.uniform(10, 1000), 2)  # Price between $10 and $1000
        sql = f"INSERT INTO products (name, category_id, price) VALUES ('{name}', {category_id}, {price});\n"
        f.write(sql)
