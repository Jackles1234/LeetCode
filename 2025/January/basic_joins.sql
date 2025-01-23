-- Write your MySQL query statement below
SELECT E.name, U.unique_id
FROM Employees E
LEFT JOIN EmployeeUNI U USING (id);

-- Write your MySQL query statement below
SELECT P.product_name, S.year, S.price
FROM Sales S
LEFT JOIN Product P USING(product_id);

-- Write your MySQL query statement below
SELECT V.customer_id, COUNT(*) AS count_no_trans
FROM Visits V
LEFT JOIN Transactions T ON (V.visit_id = T.visit_id)
WHERE T.visit_id IS NULL
GROUP BY customer_id;

-- Write your MySQL query statement below
SELECT id
FROM (
    SELECT id,temperature, LAG(temperature) OVER (ORDER BY id) AS previous_temperature
    FROM Weather)
AS WeatherLagged
WHERE previous_temperature IS NOT NULL AND previous_temperature < temperature;