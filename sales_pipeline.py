# Databricks notebook source
bronze_path = "/Volumes/dbx_training/default/sales/train.csv"

df = spark.read.option("header", "true").option("inferSchema", "true").csv(bronze_path)

df.createOrReplaceTempView("bronze_sales")

df.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE dbx_training.default.silver_sales AS
# MAGIC SELECT DISTINCT
# MAGIC     `Order ID` AS Order_ID,
# MAGIC     to_date(`Order Date`, 'dd/MM/yyyy') AS Order_Date,
# MAGIC     to_date(`Ship Date`, 'dd/MM/yyyy') AS Ship_Date,
# MAGIC     `Ship Mode` AS Ship_Mode,
# MAGIC     `Customer Name` AS Customer_Name,
# MAGIC     Segment,
# MAGIC     Region,
# MAGIC     State,
# MAGIC     City,
# MAGIC     Category,
# MAGIC     `Sub-Category` AS Sub_Category,
# MAGIC     `Product Name` AS Product_Name,
# MAGIC     try_cast(Sales AS DOUBLE) AS Sales
# MAGIC FROM bronze_sales
# MAGIC WHERE Sales IS NOT NULL
# MAGIC   AND `Order Date` IS NOT NULL

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE dbx_training.default.silver_sales AS
# MAGIC SELECT * FROM dbx_training.default.silver_sales
# MAGIC WHERE Sales IS NOT NULL

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM dbx_training.default.silver_sales LIMIT 20

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM dbx_training.default.silver_sales

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE dbx_training.default.gold_sales_summary AS
# MAGIC SELECT
# MAGIC     Region,
# MAGIC     Category,
# MAGIC     Sub_Category,
# MAGIC     YEAR(Order_Date) AS Order_Year,
# MAGIC     MONTH(Order_Date) AS Order_Month,
# MAGIC     COUNT(DISTINCT Order_ID) AS Total_Orders,
# MAGIC     ROUND(SUM(Sales), 2) AS Total_Sales,
# MAGIC     ROUND(AVG(Sales), 2) AS Avg_Sale_Value
# MAGIC FROM dbx_training.default.silver_sales
# MAGIC GROUP BY Region, Category, Sub_Category, YEAR(Order_Date), MONTH(Order_Date)
# MAGIC ORDER BY Order_Year, Order_Month

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM dbx_training.default.gold_sales_summary LIMIT 20

# COMMAND ----------

