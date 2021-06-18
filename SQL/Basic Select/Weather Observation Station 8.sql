/*
USING MS SQL
*/
select distinct city from station
where city like '[aeiou]%' AND city like '%[aeiou]';