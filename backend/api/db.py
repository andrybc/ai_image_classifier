import mysql.connector
from config import Config

def connect_db():
    """Connects to MySQL database securely"""
    try:
        conn = mysql.connector.connect(**Config.DB_CONFIG)
        return conn
    except mysql.connector.Error as e:
        print(f"❌ MySQL Connection Error: {e}")
        return None



def insert_classification(filename, category, result):
    """Inserts a classification result into the database"""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO classifications (filename, category, result) VALUES (%s, %s, %s)",
            (filename, category, result)
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Database error: {str(e)}")

def fetch_classifications():
    """Fetches the last 10 classification results"""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM classifications WHERE category = 'Animal' ORDER BY id DESC LIMIT 10")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print(f"Database error: {str(e)}")
        return []
