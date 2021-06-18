/*
USING MS SQL
*/

select distinct city from station
where city NOT like '[aeiou]%' OR  city NOT like '%[aeiou]';