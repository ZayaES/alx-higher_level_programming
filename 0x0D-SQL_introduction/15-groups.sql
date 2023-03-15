-- blah blah --
SELECT score, COUNT(*) AS number
FROM second_table
ORDER BY number DESC
GROUP BY score
