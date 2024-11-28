import random
from datetime import datetime, timedelta
import names  # You may need to install the 'names' package

# Generate 100 users
num_users = 100
start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 12, 31)

with open('insert_users.sql', 'w') as f:
    for user_id in range(1, num_users + 1):
        name = names.get_full_name().replace("'", "''")  # Escape single quotes
        email = f"user{user_id}@example.com"
        signup_date = start_date + (end_date - start_date) * random.random()
        signup_date_str = signup_date.strftime('%Y-%m-%d')
        sql = f"INSERT INTO users (name, email, signup_date) VALUES ('{name}', '{email}', '{signup_date_str}');\n"
        f.write(sql)
