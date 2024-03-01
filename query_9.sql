SELECT sb.name AS subject_name
FROM subjects sb
JOIN enrollments en ON sb.id = en.subject_id
JOIN students st ON en.student_id = st.id
WHERE st.id = 31;
-- WHERE st.id = 45;
