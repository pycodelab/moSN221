-- SQLite
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price FLOAT(4,2)
);
INSERT INTO products VALUES (1, 'Disque dur', 120.050),(2, 'Barrette de RAM',79.99);
SELECT name FROM products where id = 2;