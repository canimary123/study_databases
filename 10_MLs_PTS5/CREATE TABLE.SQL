CREATE TABLE shop_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200),
    price INT,
    stock INT,
    category VARCHAR(100)
);
