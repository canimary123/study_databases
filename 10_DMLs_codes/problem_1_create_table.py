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
    # UUID 확장 기능 활성화 (처음 한 번만 실행)
    cursor.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
    
    # students 테이블 생성
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name VARCHAR(50),
            age INT
        );
    """)
    print("students 테이블이 생성되었습니다.")

conn.commit()
conn.close()