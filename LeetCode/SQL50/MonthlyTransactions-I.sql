-- Table: Transactions

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | country       | varchar |
-- | state         | enum    |
-- | amount        | int     |
-- | trans_date    | date    |
-- +---------------+---------+
-- id is the primary key of this table.
-- The table has information about incoming transactions.
-- The state column is an enum of type ["approved", "declined"].
 

-- Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

-- Return the result table in any order.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Transactions table:
-- +------+---------+----------+--------+------------+
-- | id   | country | state    | amount | trans_date |
-- +------+---------+----------+--------+------------+
-- | 121  | US      | approved | 1000   | 2018-12-18 |
-- | 122  | US      | declined | 2000   | 2018-12-19 |
-- | 123  | US      | approved | 2000   | 2019-01-01 |
-- | 124  | DE      | approved | 2000   | 2019-01-07 |
-- +------+---------+----------+--------+------------+
-- Output: 
-- +----------+---------+-------------+----------------+--------------------+-----------------------+
-- | month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
-- +----------+---------+-------------+----------------+--------------------+-----------------------+
-- | 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
-- | 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
-- | 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
-- +----------+---------+-------------+----------------+--------------------+-----------------------+


-- Solution:
-- Write your PostgreSQL query statement below
with transactions_modified as 
(
    select id,
           country,
           state,
           amount,
           trans_date,
           to_char(trans_date,'YYYY-MM') as month
    from Transactions
)
select tbl_a.month,
       case when tbl_a.country = 'null' 
            then null
            else tbl_a.country
            end as country,
       case when tbl_a.trans_count is null 
            then 0 
            else tbl_a.trans_count
            end as trans_count,
       case when tbl_b.approved_count is null
            then 0 
            else tbl_b.approved_count
            end as approved_count,
       case when tbl_a.trans_total_amount is null
            then 0
            else tbl_a.trans_total_amount
            end as trans_total_amount,
       case when tbl_b.approved_total_amount is null
            then 0
            else tbl_b.approved_total_amount
            end as approved_total_amount
from
(
    select month,
       coalesce(country,'null') country,
       count(state) as trans_count,
       sum(amount) as trans_total_amount
    from transactions_modified 
    group by month,country
) tbl_a
left join
(
    select month,
       coalesce(country,'null') country,
       count(state) as approved_count,
       sum(amount) as approved_total_amount
    from (
            select * from transactions_modified where state='approved'
         )
    group by month,country
) tbl_b
on (
    tbl_a.month = tbl_b.month
    and tbl_a.country = tbl_b.country
)
