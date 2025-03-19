from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database connection configuration
host = 'localhost'
user = 'your_username'
password = 'your_password'
database = 'blood_bank'

# Function to search donors based on blood type and location
def search_donors(blood_type, location):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    cursor = connection.cursor()

    query = """
    SELECT donor_id, name, blood_type, location, contact_number, email
    FROM donors
    WHERE blood_type = %s AND location = %s
    """
    
    cursor.execute(query, (blood_type, location))
    donors = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return donors

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        blood_type = request.form['blood_type']
        location = request.form['location']
        
        donors = search_donors(blood_type, location)
        
        return render_template('results.html', donors=donors, blood_type=blood_type, location=location)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)