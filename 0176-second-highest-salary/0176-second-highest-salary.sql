# Write your MySQL query statement below
SELECT max(salary) AS SecondHighestSalary
From Employee
WHERE salary NOT IN(
    SELECT max(salary)
    From Employee
    );