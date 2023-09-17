# SQL Requests
## Task 1
### You need to check if the created order is displayed in the database.
For this purpose: print the list of couriers' logins with the number of their orders in «In delivery» status (field inDelivery = true).
```sql
SELECT c.login, Count (o."inDelivery") AS "Active orders",
FROM RIGHT JOIN "Orders" AS o ON c.id = o."courierId",
WHERE o."inDelivery" = true,
GROUP BY c.login;
```
## Task 2
### We need to make sure the order status database is correct.
To do this: bring out all the order trackers and their status. 
Statuses are determined by the following rule:
- if the field is finished == true, the output is 2,
- if the field canselled == true, the output is -1,
- if the inDelivery field is == true, the output is 1,
- for other cases, print 0.
```sql
SELECT track,
       CASE
           WHEN finished = TRUE THEN 2
           WHEN cancelled = TRUE THEN -1
           WHEN inDelivery = TRUE THEN 1
           ELSE 0
       END AS status
FROM "Orders";
```
