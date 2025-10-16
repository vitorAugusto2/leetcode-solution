WITH dup_rows AS (
    SELECT
        num,
        COUNT(*)
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
)

SELECT
    MAX(myn.num) AS num
FROM MyNumbers      AS myn
INNER JOIN dup_rows AS dpr ON dpr.num = myn.num;