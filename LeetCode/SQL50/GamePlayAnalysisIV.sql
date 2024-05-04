-- Table: Activity

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | player_id    | int     |
-- | device_id    | int     |
-- | event_date   | date    |
-- | games_played | int     |
-- +--------------+---------+
-- (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
-- This table shows the activity of players of some games.
-- Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 

-- Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Activity table:
-- +-----------+-----------+------------+--------------+
-- | player_id | device_id | event_date | games_played |
-- +-----------+-----------+------------+--------------+
-- | 1         | 2         | 2016-03-01 | 5            |
-- | 1         | 2         | 2016-03-02 | 6            |
-- | 2         | 3         | 2017-06-25 | 1            |
-- | 3         | 1         | 2016-03-02 | 0            |
-- | 3         | 4         | 2018-07-03 | 5            |
-- +-----------+-----------+------------+--------------+
-- Output: 
-- +-----------+
-- | fraction  |
-- +-----------+
-- | 0.33      |
-- +-----------+
-- Explanation: 
-- Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33


-- Solution:
-- Write your PostgreSQL query statement below
with number_of_players as 
(
    select count(distinct player_id) as num_players from Activity
),
first_login_dates as 
(
    select player_id, min(event_date) as event_date 
    from Activity group by player_id
)
select round(count(distinct table_a.player_id)/(select num_players 
       from number_of_players)::numeric,2) as fraction from
    (
        select A.player_id,
               B.event_date - A.event_date as diff_days
        from first_login_dates A 
             inner join 
             Activity B
             on A.player_id = B.player_id
        where B.event_date - A.event_date = 1
    ) table_a
    inner join
    (
        select A.player_id,
               B.event_date - A.event_date as diff_days
        from first_login_dates A 
             inner join 
             Activity B
             on A.player_id = B.player_id
        where B.event_date - A.event_date >= 1
    ) table_b
    on table_a.player_id = table_b.player_id
