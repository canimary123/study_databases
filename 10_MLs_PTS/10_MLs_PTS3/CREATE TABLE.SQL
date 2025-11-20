CREATE TABLE scraping_html_results (
    id SERIAL PRIMARY KEY, 
    page_title VARCHAR(500),
    page_url VARCHAR(500),
    html_length INT,
    status_code INT
);