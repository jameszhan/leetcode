## 连续出现的数字

```sql
Create table If Not Exists Logs (Id int, Num int);

Truncate table Logs;
insert into Logs (Id, Num) values ('1', '1');
insert into Logs (Id, Num) values ('2', '1');
insert into Logs (Id, Num) values ('3', '1');
insert into Logs (Id, Num) values ('4', '2');
insert into Logs (Id, Num) values ('5', '1');
insert into Logs (Id, Num) values ('6', '2');
insert into Logs (Id, Num) values ('7', '2');
```

编写一个 SQL 查询，查找所有至少连续出现三次的数字。

| Id | Num |
|----|-----|
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |

例如，给定上面的 Logs 表， 1 是唯一连续出现至少三次的数字。

| ConsecutiveNums |
|-----------------|
| 1               |


```sql
SELECT DISTINCT t1.Num AS ConsecutiveNums 
FROM Logs t1, Logs t2, Logs t3
WHERE t1.id = t2.id - 1
AND t2.id = t3.id - 1
AND t1.Num = t2.Num
AND t2.Num = t3.Num
```

```sql
SELECT Num AS ConsecutiveNums FROM Logs
GROUP BY Num
HAVING COUNT(*) >= 3
```