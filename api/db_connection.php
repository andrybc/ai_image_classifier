<?php
$servername = "localhost";
$username = "andry";
$password = "gimmedaloot";
$dbname = "projects";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    error_log("Database connection failed: " . $conn->connect_error);
    die("Database connection failed. Check the error log.");
} else {
    error_log("Database connected successfully.");
}
?>