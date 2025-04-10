from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email'):
        return jsonify({'error': 'Missing data'}), 400
    return jsonify({'message': 'User registered successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)

