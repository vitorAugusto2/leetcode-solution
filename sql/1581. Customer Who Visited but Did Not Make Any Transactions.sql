SELECT
    vis.customer_id,
    COUNT(*) AS count_no_trans
FROM Visits AS vis
LEFT JOIN Transactions AS tra ON tra.visit_id = vis.visit_id
WHERE tra.visit_id IS NULL
GROUP BY vis.customer_id;