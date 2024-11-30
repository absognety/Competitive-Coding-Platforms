/*

https://www.hackerrank.com/challenges/symmetric-pairs/problem

Oracle Solution

*/

with find_x_eq_y as (
    select x,
        y,
        count(*)
    from functions
    where x = y
    group by x,
        y
    having count(*) = 1
)
select distinct f.x,
    f.y
from functions f
    cross join functions other_f
where (
        f.x = other_f.y
        and f.y = other_f.x
    )
    and (f.x <= f.y)
    and (
        cast(f.x as varchar(10)) || '_' || cast(f.y as varchar(10))
    ) not in (
        select distinct cast(x as varchar(10)) || '_' || cast(y as varchar(10))
        from find_x_eq_y
    )
order by f.x asc;
