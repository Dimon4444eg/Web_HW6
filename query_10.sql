SELECT sub.name AS subject_name
FROM enrollments en
JOIN subjects sub ON en.subject_id = sub.id
JOIN students stu ON en.student_id = stu.id
JOIN teachers tea ON sub.teacher_id = tea.id
-- WHERE stu.id = 1 AND tea.id = 3;
WHERE stu.id = 36 AND tea.id = 5;
