CREATE TABLE news_articles (
    id SERIAL PRIMARY KEY,   -- INT AUTO_INCREMENT 대신 SERIAL 사용
    title VARCHAR(500),
    url VARCHAR(500),
    author VARCHAR(100),
    published_at DATE
);