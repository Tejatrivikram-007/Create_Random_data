import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random dates
def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Define date range
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

# Define other parameters
cities = ['New York', 'Chicago', 'Los Angeles', 'Dallas', 'Miami', 'Houston', 'San Francisco', 'Boston', 'Seattle', 'Denver']
regions = ['East', 'Midwest', 'West', 'South']
categories = ['Electronics', 'Furniture', 'Clothing']
products = ['Laptop', 'Office Chair', 'Jacket', 'Headphones', 'Sofa', 'Tablet', 'T-Shirt', 'Smartphone', 'Dining Table', 'Jeans']

# Generate data
data = []
for i in range(10000):
    order_date = random_date(start_date, end_date).strftime('%Y-%m-%d')
    customer_id = f'C{str(random.randint(1, 10000)).zfill(4)}'
    product_category = random.choice(categories)
    product_name = random.choice(products)
    quantity = random.randint(1, 10)
    unit_price = random.randint(20, 1200)
    sales_amount = quantity * unit_price
    city = random.choice(cities)
    region = random.choice(regions)

    data.append([i + 1, order_date, customer_id, product_category, product_name, quantity, unit_price, sales_amount, city, region])

# Create DataFrame
df = pd.DataFrame(data, columns=['Order ID', 'Order Date', 'Customer ID', 'Product Category', 'Product Name', 'Quantity', 'Unit Price', 'Sales Amount', 'City', 'Region'])

# Save to CSV
df.to_csv('sales_report_10000.csv', index=False)

print("CSV file created.")