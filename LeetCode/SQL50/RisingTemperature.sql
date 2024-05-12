-- Table: Weather

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the column with unique values for this table.
-- There are no different rows with the same recordDate.
-- This table contains information about the temperature on a certain day.
 

-- Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Output: 
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
-- Explanation: 
-- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).



-- Write your PostgreSQL query statement below
-- Solution
with universal_weather as 
(
    select W1.id as w1id,
        W1.recordDate as w1recorddate,
        W1.temperature as w1temperature,
        W2.id as w2id,
        W2.recordDate as w2recorddate,
        W2.temperature as w2temperature
    from Weather W1 cross join Weather W2
    where (
            (W2.id > W1.id 
              or W1.id > W2.id)
            and W2.recordDate - W1.recordDate = 1
          )
)
select distinct w2id as Id from universal_weather 
where w2temperature > w1temperature;
