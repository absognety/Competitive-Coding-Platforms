## SQL questions
### Recyclable and low fat products
Table: Products
| Column Name  | Type |
| ------------- | ------------- |
| product_id  | int  |
| recyclable  | enum  |
| low_fats    | enum  |
  
product_id is the primary key (column with unique values) for this table.  
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.  
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.  
Write a solution to find the ids of products that are both low fat and recyclable.  
Solution: `select product_id from products where low_fats='Y' and recyclable='Y';`  
  
### Find Customer Referee  
Table: Customer  

| Column Name  | Type |
| ------------- | ------------- |
| id  | int  |
| name  | varchar  |
| referee_id    | int  |  
  
In SQL, id is the primary key column for this table.  
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.  
Find the names of the customer that are not referred by the customer with id = 2.  
Return the result table in any order.  
The result format is in the following example.  
Example 1:  
Input:  
Customer table:  
  
| id | name | referee_id |  
| --- | --- | --------- |
| 1  | Will  | null |  
| 2  | Jane  | null |  
| 3  | Alex  | 2 |  
| 4  | Bill | null |  
| 5  | Zack | 1 |  
| 6  | Mark | 2 |  
  
Output:  
  
| name  |
| ------ |
| Will  |
| Jane  |
| Bill |
| Zack |  

Solution: 
```
select name from customer where referee_id != 2 or referee_id is null
```

### Article Views  
Table: Views  
| Column Name  | Type |
| ------------- | ------------- |
| article_id  | int  |
| author_id   | int  |
| viewer_id   | int  |
| view_date   | date |  
  
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.  
  
Write a solution to find all the authors that viewed at least one of their own articles.  
Return the result table sorted by id in ascending order.  
Solution:
```
select distinct derived_views.author_id as id
from (select author_id, viewer_id, count(*) as view_count 
      from views where author_id = viewer_id 
      group by author_id, viewer_id) derived_views 
where derived_views.view_count >= 1 order by derived_views.author_id;
```
