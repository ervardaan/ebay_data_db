SELECT COUNT(*) AS count
FROM (
    SELECT *
    FROM sell
    GROUP BY itemid
    HAVING COUNT(DISTINCT CATEGORYNAME) = 4
) AS subquery;
