select count(*) 
from user 
where userid in (select userid from seller) and userid in (select userid from bidder)