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
    # 1. 전체 데이터 조회
    print("\n1. 전체 학생 조회:")
    cursor.execute("SELECT * FROM students;")
    records = cursor.fetchall()
    for record in records:
        print(f"ID: {record[0]}, 이름: {record[1]}, 나이: {record[2]}")
    
    # 2. 나이가 22세 이상인 학생만 조회
    print("\n2. 나이가 22세 이상인 학생:")
    cursor.execute("SELECT * FROM students WHERE age >= 22;")
    records = cursor.fetchall()
    for record in records:
        print(f"ID: {record[0]}, 이름: {record[1]}, 나이: {record[2]}")
    
    # 3. name이 "홍길동"인 학생만 조회
    print("\n3. 이름이 '홍길동'인 학생:")
    cursor.execute("SELECT * FROM students WHERE name = '홍길동';")
    records = cursor.fetchall()
    for record in records:
        print(f"ID: {record[0]}, 이름: {record[1]}, 나이: {record[2]}")

conn.close()