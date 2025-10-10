SELECT
    emp.name,
    bon.bonus
FROM Employee   AS emp
LEFT JOIN Bonus AS bon ON bon.empId = emp.empId
WHERE (bon.bonus < 1000) OR (bon.bonus IS NULL);