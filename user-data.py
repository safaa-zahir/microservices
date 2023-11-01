from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user data (in-memory data structure for simplicity)
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    users[username] = password
    return "User registered successfully"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if users.get(username) == password:
        return "Login successful"
    return "Login failed", 401

if __name__ == '__main__':
    app.run(debug=True)
