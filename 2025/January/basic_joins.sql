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
WITH PreviousWeatherData AS
(
    SELECT 
        id,
        recordDate,
        temperature, 
        LAG(temperature, 1) OVER (ORDER BY recordDate) AS PreviousTemperature,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) AS PreviousRecordDate
    FROM 
        Weather
)
SELECT 
    id 
FROM 
    PreviousWeatherData
WHERE 
    temperature > PreviousTemperature
AND 
    recordDate = DATE_ADD(PreviousRecordDate, INTERVAL 1 DAY);

-------------------------------------------------------------
SELECT 
    w1.id
FROM 
    Weather w1
JOIN 
    Weather w2
ON 
    DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE 
    w1.temperature > w2.temperature;


--Write your MySQL query statement below
SELECT a1.machine_id, round(avg(a2.timestamp-a1.timestamp), 3) as processing_time 
FROM Activity a1
JOIN Activity a2 
ON a1.machine_id=a2.machine_id and a1.process_id=a2.process_id
AND a1.activity_type='start' and a2.activity_type='end'
GROUP BY a1.machine_id

-- Write your MySQL query statement below
SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;