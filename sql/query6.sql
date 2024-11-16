SELECT COUNT(*)
FROM user
WHERE userid IN (SELECT userid FROM seller)
  AND userid IN (SELECT userid FROM bidder);
