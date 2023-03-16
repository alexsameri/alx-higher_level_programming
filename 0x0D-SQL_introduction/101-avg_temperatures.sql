-- Displays the average temperature (in Fahrenheit)
-- By city ordered by descending temperature
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `tempreature`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
