# Amazon Customer Lifetime Value (CLV) 2.0

## 📌 Project Overview
This project predicts **Customer Lifetime Value (CLV)** for Amazon-like e-commerce data.  
It uses **RFM analysis**, **BG/NBD model**, and **Gamma-Gamma model** to estimate:
- Which customers are most valuable
- How much future revenue they will generate (next 12 months)
- Insights on customer retention and product performance

The project also includes **visualizations** and a **Power BI dashboard** for business insights.

---

## ⚙️ Features
- Customer segmentation using **RFM (Recency, Frequency, Monetary)**
- **BG/NBD model** to predict purchase probability
- **Gamma-Gamma model** to predict average order value
- **12-month CLV estimation**
- Visualizations:
  - CLV distribution
  - Revenue per product
  - Order revenue distribution
- Power BI dashboard integration

---

## 📂 Dataset
The project uses 3 CSV files:
- `customers.csv` → Customer info
- `orders.csv` → Orders data
- `products.csv` → Product catalog

Relationships:
- `orders.customer_id → customers.customer_id`
- `orders.product_id → products.product_id`

---

## 🚀 How to Run
1. Clone this repo
2. Install requirements  
   ```bash
   pip install -r requirements.txt
Run the pipeline script

python 01_amazon_clv_pipeline_v2.py


Output:

clv_summary.csv → Contains CLV per customer

Plots for CLV distribution, revenue per product, and order-level revenue

📊 Dashboard

A Power BI dashboard is created with:

CLV distribution (histogram)

Top products by revenue

Revenue trend over time

Customer-level drillthrough (details view)

📈 Business Impact

Identify high-value customers

Prioritize retention strategies

Upsell / cross-sell opportunities

Optimize marketing spend

Thank You/Let’s Connect
LinkedIn: https://www.linkedin.com/in/tanmay-sharma-800599373/
Git hub: https://github.com/Tanu272004/Amazon-CLV-2.0
