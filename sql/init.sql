CREATE DATABASE IF NOT EXISTS pet_store;
USE pet_store;

CREATE TABLE IF NOT EXISTS pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50) NOT NULL,
    age INT,
    price DECIMAL(10, 2),
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some sample data
INSERT INTO pets (name, species, age, price) VALUES 
('Buddy', 'Dog', 3, 500.00),
('Luna', 'Cat', 2, 300.00),
('Charlie', 'Parrot', 1, 150.00);
