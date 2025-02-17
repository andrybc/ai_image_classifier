-- Create a table to store image classifications

CREATE DATABASE IF NOT EXISTS projects;
USE projects;

CREATE TABLE IF NOT EXISTS ai_img_classifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL,
    result VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
