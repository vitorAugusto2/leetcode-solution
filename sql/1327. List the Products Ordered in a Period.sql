SELECT
    pro.product_name,
    SUM(ord.unit) AS unit
FROM Products    AS pro
LEFT JOIN Orders AS ord ON ord.product_id = pro.product_id
WHERE
    ord.order_date >= '2020-02-01'
    AND ord.order_date < '2020-03-01'
GROUP BY
    pro.product_name
HAVING
    SUM(ord.unit) >= 100;