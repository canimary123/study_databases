SELECT '올바른 INSERT 성공' AS status;
SELECT * FROM books;

SELECT '
PRIMARY KEY 규칙:
1. 유일성 (UNIQUE): 중복된 값을 가질 수 없음
2. NOT NULL: NULL 값을 가질 수 없음
3. 테이블당 하나: 하나의 테이블에 하나의 PRIMARY KEY
4. 식별자 역할: 각 행을 고유하게 식별
' AS primary_key_rules;