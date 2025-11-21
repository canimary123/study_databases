import psycopg2

"""PostgreSQL 데이터베이스에 연결합니다."""
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"

conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)
print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")

with conn.cursor() as cursor:
    # 먼저 이영희의 id를 조회
    cursor.execute("SELECT id FROM students WHERE name = '이영희';")
    result = cursor.fetchone()
    
    if result:
        student_id = result[0]
        print(f"이영희의 ID: {student_id}")
        
        # 나이를 25로 수정
        cursor.execute("""
            UPDATE students
            SET age = 25
            WHERE id = %s;
        """, (student_id,))
        print(f"{cursor.rowcount}개의 데이터가 UPDATE 되었습니다.")
        
        # 수정 결과 확인
        cursor.execute("SELECT * FROM students WHERE id = %s;", (student_id,))
        record = cursor.fetchone()
        print(f"\n수정 후: ID: {record[0]}, 이름: {record[1]}, 나이: {record[2]}")
    else:
        print("이영희를 찾을 수 없습니다.")

conn.commit()
conn.close()