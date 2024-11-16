select count(*) 
from seller 
where userid in (select userid 
from user 
where rating>1000)