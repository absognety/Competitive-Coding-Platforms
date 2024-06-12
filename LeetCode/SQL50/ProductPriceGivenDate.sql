-- Table: Products

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | new_price     | int     |
-- | change_date   | date    |
-- +---------------+---------+
-- (product_id, change_date) is the primary key (combination of columns with unique values) of this table.
-- Each row of this table indicates that the price of some product was changed to a new price at some date.
 
-- Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.
-- Return the result table in any order.
-- The result format is in the following example.
  
-- Example 1:

-- Input: 
-- Products table:
-- +------------+-----------+-------------+
-- | product_id | new_price | change_date |
-- +------------+-----------+-------------+
-- | 1          | 20        | 2019-08-14  |
-- | 2          | 50        | 2019-08-14  |
-- | 1          | 30        | 2019-08-15  |
-- | 1          | 35        | 2019-08-16  |
-- | 2          | 65        | 2019-08-17  |
-- | 3          | 20        | 2019-08-18  |
-- +------------+-----------+-------------+
-- Output: 
-- +------------+-------+
-- | product_id | price |
-- +------------+-------+
-- | 2          | 50    |
-- | 1          | 35    |
-- | 3          | 10    |
-- +------------+-------+

-- Write your PostgreSQL query statement below
-- Solution
with products_num as (
    select distinct product_id as product_id from Products
),
compute_dates_prices as (
    select p.product_id,
        case when bd.change_date is null then '2019-08-16'
                else bd.change_date
        end as date_of_interest,
        case when bd.new_price is null then 10
                else bd.new_price 
        end as price_of_interest 
    from products_num p left join (select * from 
    products where change_date <= '2019-08-16') bd 
    on bd.product_id = p.product_id
)
select X.product_id,
       Y.price_of_interest as price
from (
    select product_id,
        max(date_of_interest) as date 
    from compute_dates_prices group by product_id
) X inner join compute_dates_prices Y 
on X.product_id = Y.product_id and X.date = Y.date_of_interest
