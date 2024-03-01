SELECT ROUND(AVG(g.grade)) AS average_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.id
JOIN students st ON g.student_id = st.id
JOIN teachers t ON s.teacher_id = t.id
WHERE st.id = 1 AND t.id = 3;
-- WHERE st.id = 1 AND t.id = 1;
