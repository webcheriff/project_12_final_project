## Task 1
```sql
SELECT c.login, Count (o."inDelivery") AS "Active orders",
FROM RIGHT JOIN "Orders" AS o ON c.id = o."courierId",
WHERE o."inDelivery" = true,
GROUP BY c.login;
```
## Task 2
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
