/*
Using MySQL
*/
select CITY, LENGTH(CITY) from STATION 
order by LENGTH(CITY), CITY asc LIMIT 1;
select CITY, LENGTH(CITY) from STATION 
order By LENGTH(CITY) desc, CITY desc LIMIT 1;