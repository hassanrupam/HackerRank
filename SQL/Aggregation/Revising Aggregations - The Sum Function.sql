/*
USING MS SQL
*/

SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT ='California'
GROUP BY DISTRICT