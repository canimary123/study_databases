SELECT '3-1. 전체 학생 조회' AS query_name;
SELECT * FROM students;

-- 3-2. 나이가 22세 이상인 학생 조회
SELECT '3-2. 22세 이상 학생 조회' AS query_name;
SELECT * FROM students WHERE age >= 22;

-- 3-3. 이름이 "홍길동"인 학생 조회
SELECT '3-3. 홍길동 학생 조회' AS query_name;
SELECT * FROM students WHERE name = '홍길동';
