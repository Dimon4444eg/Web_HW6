SELECT ROUND(AVG(g.grade)) AS average_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.id
-- WHERE s.teacher_id = 1;
WHERE s.teacher_id = 5;