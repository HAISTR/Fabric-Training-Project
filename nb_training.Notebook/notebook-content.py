# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "31d49097-5988-40a5-b2af-498946cfbe3e",
# META       "default_lakehouse_name": "FabricTraining_LH",
# META       "default_lakehouse_workspace_id": "38e6df0f-a6db-4c1c-ba42-ca0fbe8846c6",
# META       "known_lakehouses": [
# META         {
# META           "id": "31d49097-5988-40a5-b2af-498946cfbe3e"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Read CSV file
df_orders = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/raw/orders.csv")

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col, to_date, date_format

# Cast order_date to DateType
df_orders = df_orders.withColumn(
    "order_date",
    to_date(col("order_date"))
)

display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Add year_month column in YYYY-MM format
df_orders = df_orders.withColumn(
    "year_month",
    date_format(col("order_date"), "yyyy-MM")
)
display(df_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Write as Delta Table in overwrite mode
df_orders.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("orders_bronze")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Display schema
df_orders.printSchema()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Display first 10 rows
display(df_orders.limit(10))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
