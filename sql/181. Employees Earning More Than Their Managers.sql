SELECT
    emp.name AS Employee
FROM Employee       AS emp
INNER JOIN Employee AS man ON emp.managerId = man.id
WHERE emp.salary > man.salary;