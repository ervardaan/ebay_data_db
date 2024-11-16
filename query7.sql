select count(*) 
from (select * 
from bids 
where CAST(amount AS INT)>100 
group by categoryname)