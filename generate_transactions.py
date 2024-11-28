import random
from datetime import datetime, timedelta

# Configuration
num_transactions = 10000
start_date = datetime.now() - timedelta(days=730)  # 2 years ago
end_date = datetime.now()

num_users = 100
num_products = 50

# Generate user_ids and product_ids
user_ids = list(range(1, num_users + 1))
product_ids = list(range(1, num_products + 1))

# Assuming you have product prices from the products table
# For simplicity, let's create a dictionary with product_id as key and random price
product_prices = {}
for product_id in product_ids:
    product_prices[product_id] = round(random.uniform(10, 1000), 2)

# Discounts: 9000 transactions with 0% discount, 1000 with 1%-20%
discounts_zero = [0] * 9000
discounts_non_zero = [random.randint(1, 20) for _ in range(1000)]
discounts = discounts_zero + discounts_non_zero
random.shuffle(discounts)  # Shuffle to distribute discounts randomly

# Open a file to write the INSERT statements
with open('insert_transactions.sql', 'w') as f:
    for i in range(num_transactions):
        user_id = random.choice(user_ids)
        product_id = random.choice(product_ids)
        transaction_date = start_date + (end_date - start_date) * random.random()
        transaction_date_str = transaction_date.strftime('%Y-%m-%d')
        quantity = random.randint(1, 5)
        price = product_prices[product_id]
        discount = discounts[i]
        discounted_price = price * (1 - discount / 100)
        total_price = round(discounted_price * quantity, 2)
        sql = f"INSERT INTO transactions (user_id, product_id, transaction_date, quantity, discount, total_price) VALUES ({user_id}, {product_id}, '{transaction_date_str}', {quantity}, {discount}, {total_price});\n"
        f.write(sql)
