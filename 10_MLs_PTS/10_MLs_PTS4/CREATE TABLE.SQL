CREATE TABLE keyword_search_logs (
    id SERIAL PRIMARY KEY, 
    keyword VARCHAR(200),
    result_count INT,
    search_time TIMESTAMP
);