# superstoresales-pipeline
End-to-end data analytics pipeline using Azure Data Lake, Databricks, and Power BI to transform raw sales data into an interactive business dashboard.

# Superstore Sales Analytics Pipeline

End-to-end data pipeline using Azure Data Lake Storage, Databricks, and Power BI.

## Architecture
Raw sales data → Azure Data Lake (Bronze) → Databricks (cleaning/transformation, Silver) 
→ Databricks (aggregation, Gold) → Power BI Dashboard

## Tools Used
- Azure Data Lake Storage Gen2
- Databricks (SQL, Unity Catalog)
- Power BI Desktop

## Dashboard
![Dashboard Screenshot](screenshots/dashboard_overview.png)

## Key Insights
- Total revenue: $2.24M across 8,752 orders
- West region leads in sales performance
- Phones and Chairs are top-performing sub-categories
