import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        yield client

def test_health(client):
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.get_json() == {'status': 'ok'}

def test_add_and_list_workout(client):
    # add
    resp = client.post('/api/workouts', json={'workout': 'Running', 'duration': 30})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['workout'] == 'Running'
    assert data['duration'] == 30

    # list
    resp2 = client.get('/api/workouts')
    assert resp2.status_code == 200
    workouts = resp2.get_json()
    assert isinstance(workouts, list)
    assert len(workouts) == 1
    assert workouts[0]['workout'] == 'Running'

def test_validation_errors(client):
    resp = client.post('/api/workouts', json={'workout': '', 'duration': 'abc'})
    assert resp.status_code == 400
    assert 'error' in resp.get_json()