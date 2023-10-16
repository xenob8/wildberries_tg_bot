-- Заполнение таблицы User
INSERT INTO "User" (telegram_id, user_name) VALUES
(1, 'User_1'),
(2, 'User_2'),
(3, 'User_3');

-- Заполнение таблицы Product
INSERT INTO Product (id, number, title, availability, price) VALUES
(1, 1001, 'Product_A', TRUE, 50.00),
(2, 1002, 'Product_B', TRUE, 60.00),
(3, 1003, 'Product_C', FALSE, 70.00),
(4, 1004, 'Product_D', TRUE, 80.00),
(5, 1005, 'Product_E', FALSE, 90.00),
(6, 1006, 'Product_F', TRUE, 100.00);

-- Заполнение таблицы User_Product
INSERT INTO User_Product (user_telegram_id, product_id, start_price, alert_threshold) VALUES
(1, 1, 48.00, 5),
(1, 2, 58.00, 5),
(2, 3, 68.00, 5),
(2, 4, 78.00, 5),
(3, 5, 88.00, 5),
(3, 6, 98.00, 5);
