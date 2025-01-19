-- Write your MySQL query statement below
SELECT E.name, U.unique_id
FROM Employees E
LEFT JOIN EmployeeUNI U USING (id);

-- Write your MySQL query statement below
SELECT P.product_name, S.year, S.price
FROM Sales S
LEFT JOIN Product P USING(product_id);