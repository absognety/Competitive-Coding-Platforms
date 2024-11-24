/*

https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem

*/

WITH RecursiveActiveHackers(S_DATE, H_ID) AS (
    (
        SELECT 
            h1.submission_date AS S_DATE,
            h1.hacker_id AS H_ID
        FROM (SELECT DISTINCT submission_date, hacker_id
              FROM Submissions) h1
        WHERE h1.submission_date = (SELECT MIN(submission_date) FROM (SELECT DISTINCT submission_date, hacker_id
              FROM Submissions))
    )
    UNION ALL
    (
        SELECT 
            h1.submission_date AS S_DATE,
            h1.hacker_id AS H_ID
        FROM (SELECT DISTINCT submission_date, hacker_id
              FROM Submissions) h1
        INNER JOIN RecursiveActiveHackers r
            ON h1.hacker_id = r.H_ID /*Hacker must be active on all previous days*/
           AND h1.submission_date = r.S_DATE + 1 /*Move to the next day*/
    )
),
result_set_submissions as (
    select subquery3.submission_date,
           subquery3.hacker_id,
           subquery3.name
    from
    (
        select subquery2.submission_date,
               subquery2.hacker_id,
               subquery2.name,
               DENSE_RANK() over (
                   PARTITION BY subquery2.submission_date ORDER BY subquery2.hacker_id asc
               ) RANK_by_hacker_id
        from
        (
            select subquery1.submission_date,
               subquery1.hacker_id,
               subquery1.name,
               DENSE_RANK() over (
                   PARTITION BY subquery1.submission_date ORDER BY subquery1.num_of_submissions DESC
               ) RANK_by_submissions
        FROM (
            select submissions.submission_date,
                   hackers.hacker_id,
                   hackers.name,
                   count(submissions.submission_id) as num_of_submissions
            from submissions inner join hackers on (
                submissions.hacker_id = hackers.hacker_id
            )
            where submissions.submission_id is not null 
            group by submissions.submission_date,
                   hackers.hacker_id,
                   hackers.name
        ) subquery1
        ) subquery2 where RANK_by_submissions = 1
    ) subquery3 where RANK_by_hacker_id = 1
)
SELECT 
    r.S_DATE,
    COUNT(DISTINCT r.H_ID) AS active_hackers,
    d.hacker_id AS max_submission_hacker_id,
    d.name AS max_submission_hacker_name
FROM RecursiveActiveHackers r
LEFT JOIN result_set_submissions d
    ON r.S_DATE = d.submission_date
GROUP BY r.S_DATE, d.hacker_id, d.name
ORDER BY r.S_DATE asc;
