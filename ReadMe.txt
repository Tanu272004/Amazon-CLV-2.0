# 📊 Amazon Customer Lifetime Value (CLV) Analysis

This project demonstrates an **end-to-end data analytics pipeline** for analyzing **Customer Lifetime Value (CLV)** using **Python**, **MySQL**, **Power BI**, and **Azure (Azurite)**.

---

## ✅ 📌 Project Overview
- **Goal**:  
  - Calculate CLV for Amazon customers.
  - Identify high-value customers, revenue by region, and product category performance.

- **Business Impact**:  
  - Helps prioritize retention strategies.
  - Maximizes marketing ROI by focusing on high-value customers.

---

## ✅ 🛠 Tech Stack
- **Python** → Data generation, cleaning, CLV calculation, predictive modeling.
- **MySQL** → Data storage, schema creation, advanced queries.
- **Power BI** → Dynamic dashboard for CLV visualization and segmentation.
- **Azure (Azurite)** → Cloud deployment simulation.

---

## ✅ 📂 Workflow
1. **Data Generation & CLV Calculation**
   - Used Python with `Faker` to create synthetic datasets:
     - Customers, Products, Orders, CLV table.
   - CLV calculation and predictive modeling using Linear Regression.

2. **Database Design & SQL Queries**
   - Created normalized schema with foreign keys.
   - Loaded CSVs into MySQL.
   - Queries implemented:
     - Top 10 customers by CLV
     - Revenue by region
     - CLV segmentation (High/Medium/Low)

3. **Dashboard in Power BI**
   - Connected Power BI to MySQL for dynamic reporting.
   - Key visuals:
     - KPIs: Total Revenue, Avg CLV, AOV, Customer Count
     - Top Customers by CLV
     - CLV Segmentation
     - Revenue by Region
     - AOV by Category

4. **Cloud Simulation**
   - Simulated deployment with Azure Azurite.

---

## ✅ 📊 Dashboard Preview
![Amazon CLV Dashboard](images/dashboard.png)

---

## ✅ ⚡ Key Insights
- High-value customers contribute **over 50% of revenue**.
- Top categories: **Books & Sports**.
- North America is the highest revenue region.
- Predictive CLV modeling enhances retention strategies.

---

## ✅ 📦 Installation
**1. Clone this repository**
```bash
git clone https://github.com/yourusername/amazon-clv-analysis.git
cd amazon-clv-analysis

2. Create virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
4. Run Python script

bash
Copy
Edit
python CLV.py
✅ 📚 SQL Scripts
sql/create_tables.sql → Database schema

sql/load_data.sql → Import data

sql/queries.sql → Advanced insights

✅ 🚀 Future Scope
Real-time CLV updates via Azure Data Factory.

Add churn prediction using ML pipelines.

Deploy Power BI dashboard as a web app.

✅ 🔗 Links
GitHub Repo: https://github.com/Tanu272004/Amazon_CLV_Analytics_Project#amazon_clv_analytics_project

LinkedIn Post: https://www.linkedin.com/in/tanmay-sharma-800599373/