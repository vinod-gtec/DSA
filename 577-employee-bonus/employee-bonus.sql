-- Write your PostgreSQL query statement below
Select e1.name,e2.bonus from Employee e1 left Join Bonus e2 on e1.empID=e2.empId where e2.bonus<1000 or e2.bonus is null;