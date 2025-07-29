CREATE DATABASE IF NOT EXISTS fashion_system;

USE fashion_system;

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    contact VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    nic VARCHAR(20) UNIQUE NOT NULL,
    role ENUM('Admin', 'Designer', 'Sales Manager') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Designs Table
CREATE TABLE IF NOT EXISTS designs (
    design_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    materials TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    designer VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (designer) REFERENCES users(username)
);

-- Sales Table
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    design_id INT NOT NULL,
    quantity INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    customer_info TEXT NOT NULL,
    sales_person VARCHAR(50) NOT NULL,
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (design_id) REFERENCES designs(design_id),
    FOREIGN KEY (sales_person) REFERENCES users(username)
);

--Potential Improvements
CREATE TABLE IF NOT EXISTS design_materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    design_id INT NOT NULL,
    material VARCHAR(100) NOT NULL,
    FOREIGN KEY (design_id) REFERENCES designs(design_id)
);

--Sales Calculations via Views or Triggers
CREATE VIEW sales_with_total AS
SELECT 
    s.sale_id, 
    s.design_id, 
    s.quantity,  
    (s.quantity * d.price) AS total,
    s.customer_info, 
    s.sales_person, 
    s.sale_date
FROM sales s
JOIN designs d ON s.design_id = d.design_id;

