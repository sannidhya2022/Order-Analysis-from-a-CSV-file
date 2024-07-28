import os
import pandas as pd
import datetime as dt

# Database and Redis URLs from environment variables
database_url = os.getenv('DATABASE_URL')
redis_url = os.getenv('REDIS_URL')

# Load the data
df = pd.read_csv('orders.csv')

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Extract month and year for monthly revenue calculation
df['month'] = df['order_date'].dt.to_period('M')

# Calculate total revenue per month
monthly_revenue = df.groupby('month').apply(lambda x: (x['product_price'] * x['quantity']).sum())
print("Monthly Revenue:\n", monthly_revenue)

# Calculate total revenue per product
product_revenue = df.groupby('product_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
print("\nProduct Revenue:\n", product_revenue)

# Calculate total revenue per customer
customer_revenue = df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
print("\nCustomer Revenue:\n", customer_revenue)

# Identify top 10 customers by revenue
top_10_customers = customer_revenue.sort_values(ascending=False).head(10)
print("\nTop 10 Customers by Revenue:\n", top_10_customers)
