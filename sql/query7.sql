SELECT COUNT(*)
FROM (
    SELECT *
    FROM bids
    WHERE CAST(amount AS INT) > 100
    GROUP BY categoryname
) AS subquery;
