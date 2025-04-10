from app import app

def test_register_success():
    with app.test_client() as client:
        response = client.post('/register', json={
            'username': 'sahil',
            'email': 'sahil@example.com'
        })
        assert response.status_code == 201
        assert response.get_json()['message'] == 'User registered successfully!'

def test_register_missing_data():
    with app.test_client() as client:
        response = client.post('/register', json={})
        assert response.status_code == 400
        assert response.get_json()['error'] == 'Missing data'
