SELECT COUNT(*)
FROM seller
WHERE userid IN (
    SELECT userid
    FROM user
    WHERE rating > 1000
);
