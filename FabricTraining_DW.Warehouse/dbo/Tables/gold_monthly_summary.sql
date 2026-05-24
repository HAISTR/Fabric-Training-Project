CREATE TABLE [dbo].[gold_monthly_summary] (

	[year_month] varchar(7) NULL, 
	[region] varchar(50) NULL, 
	[total_revenue] decimal(18,2) NULL, 
	[total_orders] int NULL, 
	[avg_order_value] decimal(18,2) NULL, 
	[revenue_rank_in_month] int NULL
);