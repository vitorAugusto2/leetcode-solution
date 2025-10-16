SELECT
    cus.name AS Customers
FROM Customers         AS cus
FULL OUTER JOIN Orders AS ord ON cus.id = ord.customerId
WHERE
    cus.id IS NULL OR ord.customerId IS NULL;

