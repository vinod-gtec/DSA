-- Write your PostgreSQL query statement below
Select firstName,lastName,city,state from Person p Left Join Address a on p.personId=a.personId;