-- Write your PostgreSQL query statement below
select tweet_id from tweets where length(content) > 15;
