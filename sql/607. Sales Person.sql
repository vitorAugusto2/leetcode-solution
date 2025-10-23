SELECT
    sap.name
FROM SalesPerson AS sap
WHERE sap.sales_id NOT IN (
    SELECT ord.sales_id
    FROM Orders  AS ord
    JOIN Company AS com ON ord.com_id = com.com_id AND com.name = 'RED'
)