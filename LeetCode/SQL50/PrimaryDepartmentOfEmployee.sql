-- Table: Employee

-- +---------------+---------+
-- | Column Name   |  Type   |
-- +---------------+---------+
-- | employee_id   | int     |
-- | department_id | int     |
-- | primary_flag  | varchar |
-- +---------------+---------+
-- (employee_id, department_id) is the primary key (combination of columns with unique values) for this table.
-- employee_id is the id of the employee.
-- department_id is the id of the department to which the employee belongs.
-- primary_flag is an ENUM (category) of type ('Y', 'N'). If the flag is 'Y', the department is the primary department for the employee. 
-- If the flag is 'N', the department is not the primary.
 

-- Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department 
-- is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'.

-- Write a solution to report all the employees with their primary department. For employees who belong to one department, 
-- report their only department.

-- Return the result table in any order.

-- The result format is in the following example.

-- Example 1:

-- Input: 
-- Employee table:
-- +-------------+---------------+--------------+
-- | employee_id | department_id | primary_flag |
-- +-------------+---------------+--------------+
-- | 1           | 1             | N            |
-- | 2           | 1             | Y            |
-- | 2           | 2             | N            |
-- | 3           | 3             | N            |
-- | 4           | 2             | N            |
-- | 4           | 3             | Y            |
-- | 4           | 4             | N            |
-- +-------------+---------------+--------------+
-- Output: 
-- +-------------+---------------+
-- | employee_id | department_id |
-- +-------------+---------------+
-- | 1           | 1             |
-- | 2           | 1             |
-- | 3           | 3             |
-- | 4           | 3             |
-- +-------------+---------------+
-- Explanation: 
-- - The Primary department for employee 1 is 1.
-- - The Primary department for employee 2 is 1.
-- - The Primary department for employee 3 is 3.
-- - The Primary department for employee 4 is 3.

-- Write your PostgreSQL query statement below
-- Solution
with residue_compute as 
(
    select Employee.employee_id,
           Employee.department_id 
    from Employee inner join (
        select * from       
        (
            select employee_id,
                count(department_id) as departments_cnt
            from Employee group by employee_id
        ) where departments_cnt = 1
    ) temp on Employee.employee_id = temp.employee_id
)
select employee_id,
       department_id
from Employee where primary_flag = 'Y'
UNION
(select employee_id,
       department_id 
from residue_compute);
