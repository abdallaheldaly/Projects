-- Active: 1713612195101@@127.0.0.1@3306@information_schema

SELECT 1+1;


 
BULK INSERT SchoolsTemp
    FROM '/Users/abdallahel-daly/Development/git/Power_Bi_Diploma/Graduation-Project/archive/Salaries.csv'
    WITH
    (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',  --CSV field delimiter
    ROWTERMINATOR = '\n',   --Use to shift the control to next row
    ERRORFILE = '/Users/abdallahel-daly/Development/git/Power_Bi_Diploma/Graduation-Project/archive/Salaries.csv',
    TABLOCK
    )

SELECT * FROM SchoolsTemp

SELECT AVG(BasePay) AS AverageBasePay
FROM YourTableName;


-- Which job title has the highest BasePay?

SELECT JobTitle
FROM YourTableName
WHERE BasePay = (SELECT MAX(BasePay) FROM YourTableName);


SELECT COUNT(DISTINCT JobTitle) AS NumUniqueJobTitles
FROM YourTableName;


SELECT Year, SUM(OvertimePay) AS TotalOvertimePay
FROM YourTableName
GROUP BY Year
ORDER BY Year;



SELECT Year, AVG(OtherPay) AS AverageOtherPay
FROM YourTableName
GROUP BY Year
ORDER BY AverageOtherPay DESC
LIMIT 1;






WITH RankedSalaries AS (
    SELECT
        JobTitle,
        TotalPay,
        ROW_NUMBER() OVER (PARTITION BY JobTitle ORDER BY TotalPay) AS RowAsc,
        ROW_NUMBER() OVER (PARTITION BY JobTitle ORDER BY TotalPay DESC) AS RowDesc
    FROM YourTableName
),
MedianSalaries AS (
    SELECT
        JobTitle,
        TotalPay
    FROM
        RankedSalaries
    WHERE
        RowAsc = RowDesc OR RowAsc + 1 = RowDesc
)
SELECT
    JobTitle,
    AVG(TotalPay) AS MedianTotalPay
FROM
    MedianSalaries
GROUP BY
    JobTitle
ORDER BY
    JobTitle;



SELECT MAX(Benefits) AS MaximumBenefits
FROM YourTableName;



SELECT Status, SUM(BasePay) AS TotalBasePay
FROM employees
GROUP BY Status;



SELECT EmployeeName,
       SUM(BasePay) AS TotalBasePay,
       SUM(OvertimePay) AS TotalOvertimePay,
       SUM(OtherPay) AS TotalOtherPay
FROM YourTableName
GROUP BY EmployeeName
ORDER BY EmployeeName;


SELECT EmployeeID, EmployeeName, TotalPayBenefits
FROM YourTableName
ORDER BY TotalPayBenefits DESC
LIMIT 1;

SELECT Agency, JobTitle, COUNT(EmployeeID) AS EmployeeCount
FROM YourTableName
GROUP BY Agency, JobTitle
ORDER BY Agency, JobTitle;



SELECT JobTitle, AVG(Benefits) AS AverageBenefits
FROM employees
GROUP BY JobTitle
ORDER BY AverageBenefits DESC
LIMIT 1;



SELECT Year, JobTitle, AVG(BasePay) AS AverageBasePay
FROM employees
GROUP BY Year, JobTitle
ORDER BY Year, JobTitle;


SELECT JobTitle, 
       SUM(BasePay) / SUM(TotalPayBenefits) AS BasePayToTotalPayBenefitsRatio
FROM employees
GROUP BY JobTitle;


SELECT JobTitle, 
       SUM(BasePay) / SUM(TotalPayBenefits) AS BasePayToTotalPayBenefitsRatio
FROM employees
GROUP BY JobTitle
ORDER BY BasePayToTotalPayBenefitsRatio DESC
LIMIT 1;



SELECT COUNT(DISTINCT Year) AS NumYears
FROM YourTableName;



SELECT COUNT(*) AS NumEmployees
FROM YourTableName
WHERE TotalPayBenefits > 326373.19;



SELECT Agency, AVG(TotalPayBenefits) AS AverageTotalPayBenefits
FROM YourTableName
GROUP BY Agency
ORDER BY AverageTotalPayBenefits DESC
LIMIT 1;