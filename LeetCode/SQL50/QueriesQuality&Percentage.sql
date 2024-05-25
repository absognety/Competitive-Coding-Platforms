-- Table: Queries

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | query_name  | varchar |
-- | result      | varchar |
-- | position    | int     |
-- | rating      | int     |
-- +-------------+---------+
-- This table may have duplicate rows.
-- This table contains information collected from some queries on a database.
-- The position column has a value from 1 to 500.
-- The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
 

-- We define query quality as:

-- The average of the ratio between query rating and its position.

-- We also define poor query percentage as:

-- The percentage of all queries with rating less than 3.

-- Write a solution to find each query_name, the quality and poor_query_percentage.

-- Both quality and poor_query_percentage should be rounded to 2 decimal places.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Queries table:
-- +------------+-------------------+----------+--------+
-- | query_name | result            | position | rating |
-- +------------+-------------------+----------+--------+
-- | Dog        | Golden Retriever  | 1        | 5      |
-- | Dog        | German Shepherd   | 2        | 5      |
-- | Dog        | Mule              | 200      | 1      |
-- | Cat        | Shirazi           | 5        | 2      |
-- | Cat        | Siamese           | 3        | 3      |
-- | Cat        | Sphynx            | 7        | 4      |
-- +------------+-------------------+----------+--------+
-- Output: 
-- +------------+---------+-----------------------+
-- | query_name | quality | poor_query_percentage |
-- +------------+---------+-----------------------+
-- | Dog        | 2.50    | 33.33                 |
-- | Cat        | 0.66    | 33.33                 |
-- +------------+---------+-----------------------+
-- Explanation: 
-- Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
-- Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

-- Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
-- Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33

-- Write your PostgreSQL query statement below
-- Solution

select A.query_name,
       A.quality,
       case when B.poor_query_percentage is null then 0
       else B.poor_query_percentage 
       end as poor_query_percentage
from
(
    select qc.query_name,
           round(tratios.total_ratio/qc.query_counts::numeric, 2)
        as quality
    from
    (
        select Queries.query_name,
            sum(Queries.rating/Queries.position::numeric) as total_ratio
        from Queries group by query_name
    ) tratios
    join
    (
        select query_name,
            count(query_name) as query_counts 
        from Queries group by query_name
    ) qc
    on tratios.query_name = qc.query_name
) A
left join 
(
    select qc.query_name,
        round(pqc.poor_query_counts/qc.query_counts::numeric, 4) * 100 
        as poor_query_percentage
    from
    (
        select query_name,
            count(query_name) as poor_query_counts
        from Queries where rating < 3 
        group by query_name
    ) pqc
    join
    (
        select query_name,
            count(query_name) as query_counts 
        from Queries group by query_name
    ) qc on 
    pqc.query_name = qc.query_name
) B 
on A.query_name = B.query_name
