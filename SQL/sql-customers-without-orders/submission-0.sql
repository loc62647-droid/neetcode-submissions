-- Write your query below
select c.name
from customers as c
where id not in (
    select customer_id
    from orders
)