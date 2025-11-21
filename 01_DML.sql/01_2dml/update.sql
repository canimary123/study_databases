UPDATE students 
SET age = 25 
WHERE id = 2;

SELECT '문제 4 완료: id=2 학생 나이 25로 수정됨' AS status;
SELECT * FROM students;