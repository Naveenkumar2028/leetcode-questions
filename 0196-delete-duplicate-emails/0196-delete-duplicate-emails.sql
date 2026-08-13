# Write your MySQL query statement below
DELETE p1
FROM Person p2
join person p1
ON p1.email = p2.email
        AND p1.id > p2.id;
   