def test_get_all_dogs(client):
    rv = client.get('/api/dogs/')
    assert b'[]' in rv.data or b'"name":' in rv.data
    assert rv.status_code == 200


def test_create_dog(client):
    rv = client.post('/api/dogs/', json={'id': 1, 'name': 'Snoopy'})
    assert b'Snoopy' in rv.data
    assert rv.status_code == 201


def test_get_dog(client):
    rv = client.get('/api/dogs/1')
    assert b'Snoopy' in rv.data
    assert rv.status_code == 200


def test_update_dog(client):
    rv = client.put('/api/dogs/1', json={'name': 'Scooby Doo'},)
    assert rv.status_code == 204


def test_delete_dog(client):
    rv = client.delete('/api/dogs/1')
    assert rv.status_code == 204


def test_get_dog_404(client):
    rv = client.get('/api/dogs/1')
    assert rv.status_code == 404


def test_update_dog_404(client):
    rv = client.put('/api/dogs/1', json={'name': 'Scooby Doo'},)
    assert rv.status_code == 404


def test_delete_dog_404(client):
    rv = client.delete('/api/dogs/1')
    assert rv.status_code == 404
