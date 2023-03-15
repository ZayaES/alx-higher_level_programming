-- blah blah --
INSERT INTO second_table (id, name, score) VALUES (5, '', 12);
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
