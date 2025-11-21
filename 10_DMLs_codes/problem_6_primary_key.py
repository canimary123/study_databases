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
    # books 테이블 생성
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INT PRIMARY KEY,
            title VARCHAR(100),
            price INT
        );
    """)
    print("books 테이블이 생성되었습니다.\n")
    
    # 첫 번째 INSERT (성공)
    try:
        cursor.execute("""
            INSERT INTO books (book_id, title, price)
            VALUES (1, '책 A', 10000);
        """)
        print("✅ 첫 번째 INSERT 성공: book_id=1, title='책 A'")
        conn.commit()
    except Exception as e:
        print(f"❌ 첫 번째 INSERT 실패: {e}")
        conn.rollback()
    
    # 두 번째 INSERT (실패 - 중복된 PRIMARY KEY)
    try:
        cursor.execute("""
            INSERT INTO books (book_id, title, price)
            VALUES (1, '책 B', 15000);
        """)
        print("✅ 두 번째 INSERT 성공: book_id=1, title='책 B'")
        conn.commit()
    except Exception as e:
        print(f"\n❌ 두 번째 INSERT 실패!")
        print(f"에러 메시지: {e}\n")
        conn.rollback()

conn.close()

print("=" * 60)
print("📚 PRIMARY KEY 설명")
print("=" * 60)
print("""
❓ 어떤 에러가 발생하는가?
→ duplicate key value violates unique constraint "books_pkey"

❓ 왜 발생하는가?
→ book_id가 PRIMARY KEY이기 때문에 같은 값(1)을 중복해서 INSERT 할 수 없습니다.

📌 PRIMARY KEY의 규칙:
1. 유일성 (UNIQUE): 테이블 내에서 중복된 값을 가질 수 없음
2. NOT NULL: NULL 값을 가질 수 없음
3. 하나의 테이블에 하나의 PRIMARY KEY만 존재
4. 각 행을 고유하게 식별하는 역할
""")