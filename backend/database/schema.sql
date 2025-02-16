-- Create a table to store image classifications
CREATE TABLE ai_img_classifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL,
    result VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
