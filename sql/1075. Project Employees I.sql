SELECT
    pro.project_id,
    ROUND(
        AVG(emp.experience_years), 2
    ) AS average_years
FROM Project       AS pro
LEFT JOIN Employee AS emp ON emp.employee_id = pro.employee_id
GROUP BY pro.project_id
ORDER BY pro.project_id ASC;