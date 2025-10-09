SELECT
    usr.name,
    SUM(tra.amount) AS balance
FROM Users              AS usr
LEFT JOIN Transactions  AS tra ON usr.account = tra.account
GROUP BY usr.name
HAVING SUM(tra.amount) > 10000;