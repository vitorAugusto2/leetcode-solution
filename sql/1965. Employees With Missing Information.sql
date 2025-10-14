SELECT
    COALESCE(emp.employee_id, sal.employee_id) AS employee_id
FROM Employees           AS emp
FULL OUTER JOIN Salaries AS sal ON sal.employee_id = emp.employee_id
WHERE
    emp.employee_id IS NULL OR sal.employee_id IS NULL
ORDER BY employee_id ASC;