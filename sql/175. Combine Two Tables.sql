SELECT
    per.firstName,
    per.lastName,
    add.city,
    add.state
FROM Person         AS per
LEFT JOIN Address   AS add ON per.personId = add.personId;