-- 2. Isey refresh karne ke liye Stored Procedure banate hain
CREATE PROCEDURE RefreshGoldSummary
AS
BEGIN
    -- Purana data hatao
    TRUNCATE TABLE gold_monthly_summary;

    -- Naya data calculate karke dalo
    WITH MonthlyStats AS (
        SELECT 
            FORMAT(f.order_date, 'yyyy-MM') AS year_month,
            c.region,
            SUM(f.total_amount) AS total_revenue,
            COUNT(f.order_id) AS total_orders,
            CAST(SUM(f.total_amount) / COUNT(f.order_id) AS DECIMAL(18,2)) AS avg_order_value
        FROM 
            fact_orders f
        JOIN 
            dim_customer c ON f.customer_id = c.customer_id
        GROUP BY 
            FORMAT(f.order_date, 'yyyy-MM'), 
            c.region
    )
    INSERT INTO gold_monthly_summary (year_month, region, total_revenue, total_orders, avg_order_value, revenue_rank_in_month)
    SELECT 
        year_month,
        region,
        total_revenue,
        total_orders,
        avg_order_value,
        RANK() OVER(PARTITION BY year_month ORDER BY total_revenue DESC) AS revenue_rank_in_month
    FROM 
        MonthlyStats;
END;