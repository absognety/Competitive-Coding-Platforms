-- Table: Logs

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- In SQL, id is the primary key for this table.
-- id is an autoincrement column.
 
-- Find all numbers that appear at least three times consecutively.

-- Return the result table in any order.

-- The result format is in the following example.

-- Example 1:

-- Input: 
-- Logs table:
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+
-- Output: 
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- Explanation: 1 is the only number that appears consecutively for at least three times.

-- Write your PostgreSQL query statement below
-- Solution
with computed_tb as (
    select X.id Xid,
            X.num Xnum,
            Y.id Yid,
            Y.num Ynum,
            Y.id - X.id as diff
        from Logs X cross join Logs Y 
        where Y.id - X.id in (1) and X.num = Y.num
)
select distinct A.Xnum as ConsecutiveNums
from computed_tb A join computed_tb B on (A.Xid = B.Yid) 
where A.Xnum in (
    select Xnum from computed_tb group by Xnum having count(Xnum) >= 2
)
