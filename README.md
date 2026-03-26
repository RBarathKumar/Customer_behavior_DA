# Customer_behavior_DA
Here’s a **polished, recruiter-friendly README** tailored to your actual project files and workflow:

---

# 📊 Customer Shopping Behavior Analysis

## 🔍 Overview

This project presents an end-to-end data analytics workflow using a customer shopping behavior dataset. It covers data preprocessing, exploratory data analysis (EDA), SQL-based insights, and interactive dashboard creation.

The goal is to extract meaningful insights about customer purchasing patterns, revenue distribution, and behavioral trends to support data-driven decision-making.

---

## 📁 Dataset

* **File:** `customer_shopping_behavior.csv`
* Contains customer-level transactional data including:

  * Demographics (age, gender)
  * Purchase details (items, amount, frequency)
  * Customer behavior (subscription, previous purchases)
  * Ratings and discounts

---

## 🛠️ Tools & Technologies

* **Python (Pandas)** – Data loading, cleaning, and feature engineering
* **MySQL** – Querying and analytical insights
* **Power BI** – Interactive dashboard creation
* **Gamma** – Presentation (PPT) generation
* **Jupyter Notebook / PyCharm** – Development environment

---

## ⚙️ Project Steps

### 1. Data Loading

* Loaded dataset using Pandas.
* Inspected structure and column formats.

### 2. Data Cleaning & Transformation

* Filled missing review ratings using median per category.
* Standardized column names (lowercase, underscores).
* Renamed columns for consistency.
* Removed unnecessary columns (e.g., promo code).
* Created new features:

  * **Age Groups** (Young Adult, Adult, Middle-aged, Senior)
  * **Purchase Frequency (Days)** mapped from categorical values

### 3. Exploratory Data Analysis (EDA)

* Analyzed distributions of customer demographics and purchases.
* Identified trends in ratings, spending, and frequency.
* Detected patterns across categories and customer segments.

### 4. SQL Analysis (MySQL)

* Loaded cleaned data into MySQL using SQLAlchemy.
* Performed analytical queries such as:

  * Revenue by gender
  * High-value discounted purchases
  * Top-rated products
  * Shipping type comparison
  * Subscription vs non-subscription spending
  * Customer segmentation (New, Returning, Loyal)
  * Revenue by age group

### 5. Dashboard Development

* Built an interactive Power BI dashboard to visualize:

  * Revenue trends
  * Customer segmentation
  * Product performance
  * Purchase behavior insights

### 6. Reporting & Presentation

* Compiled insights into a structured report.
* Created a presentation using Gamma for stakeholder communication.

---

## 📊 Dashboard

* Power BI dashboard file: `Customer_behavior Dashboard.pbix`
* Key features:

  * KPI cards (Total Revenue, Avg Purchase, etc.)
  * Category and product-level insights
  * Customer segmentation visuals
  * Filters for dynamic analysis

---

## 📈 Results & Insights

* Identified key revenue drivers across customer segments.
* Found differences in spending behavior between subscribers and non-subscribers.
* Highlighted top-performing products based on ratings and purchases.
* Segmented customers into actionable groups (New, Returning, Loyal).
* Revealed trends in purchase frequency and discount usage.

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd <project-folder>
```

### 2. Install Dependencies

```bash
pip install pandas sqlalchemy pymysql
```

### 3. Run Python Script

* Open `Customer.py`
* Update MySQL credentials:

```python
username="root"
password="root"
host="localhost"
port="3306"
database="customer_behavior"
```

* Run the script to:

  * Clean data
  * Create features
  * Load data into MySQL

### 4. Run SQL Queries

* Open `CustomerDA.sql` in MySQL Workbench
* Execute queries for analysis

### 5. Open Dashboard

* Open `Customer_behavior Dashboard.pbix` in Power BI Desktop

### 6. View Presentation

* Open Gamma-generated PPT for summary insights

---

## 📌 Key Takeaways

* End-to-end data analytics pipeline implementation
* Strong use of Python for data preprocessing and feature engineering
* Advanced SQL for business insights
* Effective data storytelling using Power BI and presentations

---


