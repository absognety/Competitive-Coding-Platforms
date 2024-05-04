-- Table: Seat

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | student     | varchar |
-- +-------------+---------+
-- id is the primary key (unique value) column for this table.
-- Each row of this table indicates the name and the ID of a student.
-- id is a continuous increment.
 

-- Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

-- Return the result table ordered by id in ascending order.

-- The result format is in the following example.

-- Example 1:

-- Input: 
-- Seat table:
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Abbot   |
-- | 2  | Doris   |
-- | 3  | Emerson |
-- | 4  | Green   |
-- | 5  | Jeames  |
-- +----+---------+
-- Output: 
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Doris   |
-- | 2  | Abbot   |
-- | 3  | Green   |
-- | 4  | Emerson |
-- | 5  | Jeames  |
-- +----+---------+
-- Explanation: 
-- Note that if the number of students is odd, there is no need to change the last one's seat.



-- Solution
-- Write your PostgreSQL query statement below

with consecutive_students as 
(
    select S1.id S1id, 
       S2.id S2id, 
       S1.student S1student, 
       S2.student S2student 
    from Seat S1 cross join Seat S2
    where S2.id - S1.id = 1
),
non_overlapping_students as 
(
    select tbl.S1student,
           tbl.S2student
    from 
    (
        select S1id,
           S2id,
           S1student,
           S2student,
           row_number() over () as row_number
        from consecutive_students
    ) tbl
    where MOD(tbl.row_number,2) != 0
),
swap_seats as
(
    select row_number() over () as row_number, student from
    (
        select UNNEST(STRING_TO_ARRAY(students, ',')) as student from 
                (
                    select S2student || ',' || S1student as students 
                    from non_overlapping_students
                )
    )
),
last_seat as 
(
    select id as row_number,student from Seat 
    where id = (select max(id) from Seat)
)
select id,student from
(
    select row_number as id,
        student,
        dense_rank() over (
            partition by student 
            order by row_number
        ) as rank
    from
    (
        select row_number,student from swap_seats
        UNION ALL
        select row_number,student from last_seat
    )
) where rank=1 order by id
