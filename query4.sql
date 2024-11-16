select distinct(itemid) 
from item 
where CAST(currently as INT)=(select max(currently) 
from (select CAST(currently AS INT) AS currently,itemid 
from item))