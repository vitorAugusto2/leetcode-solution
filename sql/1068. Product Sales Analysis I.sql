SELECT
    pro.product_name,
    sal.year,
    sal.price
FROM Sales        AS sal
LEFT JOIN Product AS pro ON pro.product_id = sal.product_id