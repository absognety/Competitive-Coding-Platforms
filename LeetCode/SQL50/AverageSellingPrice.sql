-- Table: Prices

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | start_date    | date    |
-- | end_date      | date    |
-- | price         | int     |
-- +---------------+---------+
-- (product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
-- Each row of this table indicates the price of the product_id in the period from start_date to end_date.
-- For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.

-- Table: UnitsSold

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | purchase_date | date    |
-- | units         | int     |
-- +---------------+---------+
-- This table may contain duplicate rows.
-- Each row of this table indicates the date, units, and product_id of each product sold. 
 
-- Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.

-- Return the result table in any order.

-- The result format is in the following example.

-- Example 1:

-- Input: 
-- Prices table:
-- +------------+------------+------------+--------+
-- | product_id | start_date | end_date   | price  |
-- +------------+------------+------------+--------+
-- | 1          | 2019-02-17 | 2019-02-28 | 5      |
-- | 1          | 2019-03-01 | 2019-03-22 | 20     |
-- | 2          | 2019-02-01 | 2019-02-20 | 15     |
-- | 2          | 2019-02-21 | 2019-03-31 | 30     |
-- +------------+------------+------------+--------+
-- UnitsSold table:
-- +------------+---------------+-------+
-- | product_id | purchase_date | units |
-- +------------+---------------+-------+
-- | 1          | 2019-02-25    | 100   |
-- | 1          | 2019-03-01    | 15    |
-- | 2          | 2019-02-10    | 200   |
-- | 2          | 2019-03-22    | 30    |
-- +------------+---------------+-------+
-- Output: 
-- +------------+---------------+
-- | product_id | average_price |
-- +------------+---------------+
-- | 1          | 6.96          |
-- | 2          | 16.96         |
-- +------------+---------------+
-- Explanation: 
-- Average selling price = Total Price of Product / Number of products sold.
-- Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
-- Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96


-- Write your PostgreSQL query statement below
-- Solution
with data_prepare as 
(
    select Prices.product_id,
           Prices.start_date,
           Prices.end_date,
           Prices.price,
           UnitsSold.purchase_date,
           UnitsSold.units,
           case when UnitsSold.units is null 
           then 0
           else Prices.price * UnitsSold.units 
           end as total_price
    from Prices left join UnitsSold 
    on Prices.product_id = UnitsSold.product_id
    where (UnitsSold.purchase_date is null)
           or
          (UnitsSold.purchase_date >= Prices.start_date 
          and UnitsSold.purchase_date <= Prices.end_date)
),
total_units_sold as 
(
    select product_id,
           sum(units) as total_units_sold
    from UnitsSold group by product_id
)
select a.product_id,
       case when a.total_price = 0 then 0
       else round(a.total_price/b.total_units_sold::numeric, 2) 
       end as average_price
from
(
    select product_id,
       sum(total_price) as total_price
    from data_prepare group by product_id
) a
left join
total_units_sold b on a.product_id = b.product_id;
