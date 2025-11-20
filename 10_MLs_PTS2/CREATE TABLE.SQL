-- 1. 기존에 있는(잘못된) 테이블 삭제
DROP TABLE IF EXISTS web_links;

-- 2. 자동 증가(SERIAL) 기능 넣어서 다시 생성
CREATE TABLE web_links (
    id SERIAL PRIMARY KEY,      -- ★ 중요: INT 대신 SERIAL 사용
    link_text VARCHAR(200),
    link_url VARCHAR(500),
    category VARCHAR(100)
);