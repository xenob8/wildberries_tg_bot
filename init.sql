-- Создание таблицы User
CREATE TABLE "User" (
    telegram_id INT PRIMARY KEY,
    user_name TEXT NOT NULL
);

-- Создание таблицы Product
CREATE TABLE Product (
    id INT PRIMARY KEY,
    number INT NOT NULL,
    title TEXT NOT NULL,
    availability BOOLEAN NOT NULL,
    price MONEY NOT NULL
);

-- Создание таблицы User_Product
CREATE TABLE User_Product (
    user_telegram_id INT REFERENCES "User"(telegram_id),
    product_id INT REFERENCES Product(id),
    start_price MONEY NOT NULL,
    alert_threshold INT NOT NULL,
    PRIMARY KEY (user_telegram_id, product_id)
);
