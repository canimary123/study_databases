-- UUID primary key 사용
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE users_uuid_name (
  id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100)
);


INSERT INTO users_uuid_name (name) VALUES ('Alice');
VALUES
('Alice'),
('Bob'),
('Charlie');

SELECT id _name, name from users_uuid_name;



update users_uuid_name
set name = 'Updated Name'
where id_name = '34f056a6-d123-4640-977b-7f86fdf3630e';