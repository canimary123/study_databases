import psycopg2
"""PostgreSQL 데이터베이스에 연결합니다."""
try:
    # 환경 변수 또는 기본값으로 데이터베이스 연결 정보 설정
    db_host = os.getenv("DB_HOST", "db_postgresql")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("POSTGRES_DB", "main_db")
    db_user = os.getenv("POSTGRES_USER", "admin")
    db_password = os.getenv("POSTGRES_PASSWORD", "admin123")
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")
    # return conn
except psycopg2.OperationalError as e:
    print(f"데이터베이스 연결에 실패했습니다: {e}")
    print("연결 정보를 확인하거나 Docker 컨테이너가 실행 중인지 확인하세요.")












