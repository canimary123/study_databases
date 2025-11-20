-- CREATE TABLE study_webscripings_database (
--     contents varchar(500),
--     link varchar(500),
--     link_html varchar(500),
--     link_href varchar(500)
-- );



CREATE TABLE study_webscripings_database (
    id SERIAL PRIMARY KEY,
    contents TEXT,
    link TEXT,
    link_html TEXT,
    link_href TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

SELECT *
FROM study_webscripings_database;