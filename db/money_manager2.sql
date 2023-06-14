DROP TABLE tags;
DROP TABLE merchants;
DROP TABLE transactions;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255)
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount INT,
    merchant_id INT NOT NULL REFERENCES ON DELETE CASCADE merchants(id) ,
    tag_id INT NOT NULL REFERENCES ON DELETE CASCADE tags(id)
);
