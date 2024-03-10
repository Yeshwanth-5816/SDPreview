from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Replace these values with your PostgreSQL database credentials
db_host = "localhost"
db_port = "5432"
db_name = "music"
db_user = "postgres"
db_password = "johnwick"

def check_username_existence(username):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        )

        cursor = connection.cursor()

        # Check if the username exists in the 'users' table
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))

        user_exists = cursor.fetchone() is not None

        connection.close()

        return user_exists

    except Exception as e:
        print("Error:", e)
        return False

@app.route('/check-username', methods=['POST'])
def check_username():
    data = request.get_json()
    username = data.get('username', '')

    # Check if the username already exists in the database
    username_exists = check_username_existence(username)

    return jsonify({'exists': username_exists})

if __name__ == '__main__':
    app.run(debug=True)
