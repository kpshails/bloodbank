from flask import Flask
from flask_mysql_connector import MySQL
import os

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD", "roots")  # Use env variable for security
app.config['MYSQL_DATABASE'] = 'blood_bank'

mysql = MySQL(app)

@app.route('/')
def home():
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        return f"MySQL Connected to {db_name[0]}"
    except Exception as e:
        return f"Error: {str(e)}"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
