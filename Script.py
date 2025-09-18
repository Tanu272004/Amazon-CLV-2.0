# 01_amazon_clv_pipeline_v2.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from lifetimes import BetaGeoFitter, GammaGammaFitter
from lifetimes.utils import summary_data_from_transaction_data

# --- Step 1: Load Data ---
customers = pd.read_csv(r"T:\GitHub\Financial report\Amazon.Scripts\Amazon-CLV\CSV\customers.csv")
orders = pd.read_csv(r"T:\GitHub\Financial report\Amazon.Scripts\Amazon-CLV\CSV\orders.csv")
products = pd.read_csv(r"T:\GitHub\Financial report\Amazon.Scripts\Amazon-CLV\CSV\products.csv")

print("Customers:", customers.shape)
print("Orders:", orders.shape)
print("Products:", products.shape)

# --- Step 2: Data Cleaning ---
orders['order_date'] = pd.to_datetime(orders['order_date'])

# Merge orders with products
orders = orders.merge(products, on="product_id", how="left")

# Check if revenue column already exists
if 'revenue' not in orders.columns:
    # Automatically detect price column
    price_cols = [col for col in orders.columns if 'price' in col.lower()]
    if not price_cols:
        raise ValueError("No price column found in orders/products after merge!")
    price_col = price_cols[0]

    # Compute revenue
    orders['revenue'] = orders['quantity'] * orders[price_col]
else:
    print("Revenue column already exists, using existing values.")

# --- Step 3: Aggregate to Customer Level ---
snapshot_date = orders['order_date'].max() + pd.Timedelta(days=1)

rfm = orders.groupby('customer_id').agg({
    'order_date': lambda x: (snapshot_date - x.max()).days,   # Recency
    'order_id': 'count',                                     # Frequency
    'revenue': 'sum'                                         # Monetary
}).rename(columns={
    'order_date': 'recency',
    'order_id': 'frequency',
    'revenue': 'monetary'
}).reset_index()

print("RFM sample:\n", rfm.head())

# --- Step 4: Prepare for Lifetimes ---
transactions = orders[['customer_id', 'order_date', 'revenue']]

summary = summary_data_from_transaction_data(
    transactions,
    customer_id_col='customer_id',
    datetime_col='order_date',
    monetary_value_col='revenue',
    observation_period_end=snapshot_date
)

print("Summary sample:\n", summary.head())

# --- Step 5: Fit BG/NBD Model ---
bgf = BetaGeoFitter(penalizer_coef=0.001)
bgf.fit(summary['frequency'], summary['recency'], summary['T'])

# --- Step 6: Fit Gamma-Gamma Model ---
ggf = GammaGammaFitter(penalizer_coef=0.01)
ggf.fit(summary['frequency'], summary['monetary_value'])

# Predict Customer Lifetime Value (CLV)
summary['clv'] = ggf.customer_lifetime_value(
    bgf,
    summary['frequency'],
    summary['recency'],
    summary['T'],
    summary['monetary_value'],
    time=12,  # months
    freq='D'
)

print("CLV summary:\n", summary[['clv']].describe())

# --- Step 7: Visualization ---
plt.figure(figsize=(10,6))
sns.histplot(summary['clv'], bins=50, kde=True)
plt.title("Customer Lifetime Value Distribution")
plt.xlabel("CLV")
plt.ylabel("Count")
plt.show()

product_revenue = orders.groupby('product_id')['revenue'].sum().reset_index()
plt.figure(figsize=(12,6))
sns.barplot(x='product_id', y='revenue', data=product_revenue)
plt.title("Revenue per Product")
plt.xlabel("Product ID")
plt.ylabel("Total Revenue")
plt.show()

plt.figure(figsize=(12,6))
sns.histplot(orders['revenue'], bins=50, kde=True)
plt.title("Revenue Distribution per Order")
plt.xlabel("Revenue")
plt.ylabel("Count")
plt.show()

# --- Step 8: Save CLV summary to CSV ---
output_path = r"T:\GitHub\Financial report\Amazon.Scripts\Amazon-CLV\CSV\clv_summary.csv"
summary.reset_index().to_csv(output_path, index=False)
print(f"✅ CLV summary saved to {output_path}")

print("✅ Amazon CLV 2.0 pipeline executed successfully!")
