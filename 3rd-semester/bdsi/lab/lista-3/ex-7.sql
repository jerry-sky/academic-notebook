WITH RECURSIVE bc(n, k, val) AS (
    SELECT 0, 0, 1
    UNION ALL
    SELECT (CASE k WHEN n THEN n + 1 ELSE n END),
           (CASE k WHEN n THEN 0 ELSE k + 1 END),
           (CASE k
                WHEN n THEN 1
                WHEN 0 THEN 1
                ELSE (SELECT SUM(a.val) FROM bc AS a WHERE a.n = n - 1 AND a.k IN (k, k - 1)) END)
#                 ELSE val END)
#                 ELSE LAST_VALUE(val) over (order by val) END)
    FROM bc
    WHERE n < 15
)
SELECT *
FROM bc;


