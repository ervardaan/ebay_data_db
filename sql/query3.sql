select count(*) AS count 
from (select * from sell 
group by itemid 
having COUNT(DISTINCT CATEGORYNAME) = 4)