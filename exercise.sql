-- find duplicates
select email as Email
from Person
group by email
having count(id) > 1

-- combine two tables
select firstName, lastName, city, state
from Person
left outer join Address on Person.personId = Address.personId 

-- self join
select T1.name as Employee
from Employee as T1, Employee as T2
where T1.managerId = T2.id and T1.salary > T2.salary

-- Anti Join
select name as Customers
from Customers
where not exists (
    select *
    from Orders
    where Orders.customerId = Customers.id
)

-- Comparison with previous value
select w1.id
from Weather as w1, Weather as w2
where w2.recordDate = Date_add(w1.recordDate, Interval -1 day) and w1.temperature > w2.temperature

-- Join and Where and null
select name, bonus
from Employee
left join Bonus on Employee.empId = Bonus.empId
where bonus < 1000 or bonus is null

-- find the customer with the most orders
select customer_number 
from Orders 
group by customer_number
order by count(order_number) desc
limit 1

-- Find biggest single number
SELECT COALESCE((SELECT num 
FROM MyNumbers
GROUP BY num
HAVING COUNT(num) =1
ORDER BY num DESC
LIMIT 1),null)
AS num