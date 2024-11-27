/*

https://www.hackerrank.com/challenges/placements

Solution: Oracle

*/

select name from 
(
    select s1.id as id,
           s2.id as friend_id,
           s1.name as name,
           s2.name as friend_name,
           p1.salary as salary,
           p2.salary as friend_salary
    from students s1 
         cross join students s2 
         join packages p1 on (
             s1.id = p1.id
         )
         join packages p2 on (
             s2.id = p2.id
         )
    where s1.id != s2.id and (cast(s1.id as varchar(10)) || '_' || cast(s2.id as varchar(10))) in (
        select cast(id as varchar(10)) || '_' || cast(friend_id as varchar(10)) from friends 
    )
) where friend_salary > salary order by friend_salary asc;
