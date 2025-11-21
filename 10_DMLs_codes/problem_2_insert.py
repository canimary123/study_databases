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
    # 데이터 INSERT (id는 자동 생성)
    cursor.execute("""
        INSERT INTO students (name, age) VALUES
        ('홍길동', 23),
        ('이영희', 21),
        ('박철수', 26);
    """)
    print(f"{cursor.rowcount}개의 데이터가 INSERT 되었습니다.")
    
    # 확인용 SELECT
    cursor.execute("SELECT * FROM students;")
    records = cursor.fetchall()
    print("\n현재 students 테이블 데이터:")
    for record in records:
        print(record)

conn.commit()
conn.close()