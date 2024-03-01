SELECT st.name AS student_name, g.grade
FROM grades g
JOIN students st ON g.student_id = st.id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups gr ON st.group_id = gr.id
WHERE gr.id = 3 AND sub.id = 2
ORDER BY g.date DESC
LIMIT 1;
-- WHERE gr.id = 1 AND sub.id = 9
-- ORDER BY g.date DESC
-- LIMIT 3;
