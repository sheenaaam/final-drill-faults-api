import pytest
from main import app, db
from models import Fault

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_create_fault(client):
    response = client.post('/api/faults/', json={
        'student_id': 1,
        'description': 'Cheating during exam',
        'date_reported': '2025-05-29',
        'resolved': False
    })
    assert response.status_code == 201

def test_get_faults(client):
    client.post('/api/faults/', json={
        'student_id': 1,
        'description': 'Late homework',
        'date_reported': '2025-05-29',
        'resolved': False
    })
    response = client.get('/api/faults/')
    assert response.status_code == 200
    assert len(response.json) > 0
