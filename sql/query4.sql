SELECT DISTINCT(itemid)
FROM item
WHERE CAST(currently AS INT) = (
    SELECT MAX(currently)
    FROM (
        SELECT CAST(currently AS INT) AS currently, itemid
        FROM item
    ) AS subquery
);
