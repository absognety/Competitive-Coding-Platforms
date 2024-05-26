-- Table: Accounts

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | account_id  | int  |
-- | income      | int  |
-- +-------------+------+
-- account_id is the primary key (column with unique values) for this table.
-- Each row contains information about the monthly income for one bank account.
 

-- Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

-- "Low Salary": All the salaries strictly less than $20000.
-- "Average Salary": All the salaries in the inclusive range [$20000, $50000].
-- "High Salary": All the salaries strictly greater than $50000.
-- The result table must contain all three categories. If there are no accounts in a category, return 0.

-- Return the result table in any order.

-- The result format is in the following example.

-- Example 1:

-- Input: 
-- Accounts table:
-- +------------+--------+
-- | account_id | income |
-- +------------+--------+
-- | 3          | 108939 |
-- | 2          | 12747  |
-- | 8          | 87709  |
-- | 6          | 91796  |
-- +------------+--------+
-- Output: 
-- +----------------+----------------+
-- | category       | accounts_count |
-- +----------------+----------------+
-- | Low Salary     | 1              |
-- | Average Salary | 0              |
-- | High Salary    | 3              |
-- +----------------+----------------+
-- Explanation: 
-- Low Salary: Account 2.
-- Average Salary: No accounts.
-- High Salary: Accounts 3, 6, and 8.


-- Write your PostgreSQL query statement below
-- Solution

select category,
       count(account_id) as accounts_count
from (
    select account_id,
        income,
        case when income < 20000 then 'Low Salary' 
        when income > 50000 
        then 'High Salary'
        when income >= 20000 and income <= 50000 
        then 'Average Salary' 
        end as category
    from Accounts
) group by category
UNION ALL
select 'Average Salary' catgeory, 0 accounts_count
WHERE NOT EXISTS (SELECT 1 FROM Accounts 
WHERE income >= 20000 and income <= 50000)
UNION ALL 
select 'Low Salary' catgeory, 0 accounts_count
WHERE NOT EXISTS (SELECT 1 FROM Accounts 
WHERE income < 20000)
UNION ALL
select 'High Salary' catgeory, 0 accounts_count
WHERE NOT EXISTS (SELECT 1 FROM Accounts 
WHERE income > 50000)
