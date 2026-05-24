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

# MAGIC %%sql
# MAGIC DESCRIBE DETAIL orders_bronze;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC OPTIMIZE orders_bronze ZORDER BY (order_date);

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC VACUUM orders_bronze RETAIN 168 HOURS;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE HISTORY orders_bronze;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC ANALYZE TABLE orders_bronze COMPUTE STATISTICS;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
