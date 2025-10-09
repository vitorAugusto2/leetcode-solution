SELECT
    emu.unique_id,
    emp.name
FROM Employees        AS emp
LEFT JOIN EmployeeUNI AS emu ON emp.id = emu.id;