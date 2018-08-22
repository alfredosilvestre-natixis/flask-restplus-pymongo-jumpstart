def test_get_all_dogs(client):
    rv = client.get('/api/dogs/')

    if b'[]' not in rv.data:
        raise AssertionError(rv.data)
    if rv.status_code != 200:
        raise AssertionError(rv.status_code)


def test_create_dog(client):
    rv = client.post('/api/dogs/', json={'id': 1, 'name': 'Snoopy'})

    if b'Snoopy' not in rv.data:
        raise AssertionError(rv.data)
    if rv.status_code != 201:
        raise AssertionError(rv.status_code)


def test_get_dog(client):
    rv = client.get('/api/dogs/1')

    if b'Snoopy' not in rv.data:
        raise AssertionError(rv.data)
    if rv.status_code != 200:
        raise AssertionError(rv.status_code)


def test_update_dog(client):
    rv = client.put('/api/dogs/1', json={'name': 'Scooby Doo'})

    if rv.status_code != 204:
        raise AssertionError(rv.status_code)


def test_delete_dog(client):
    rv = client.delete('/api/dogs/1')

    if rv.status_code != 204:
        raise AssertionError(rv.status_code)


def test_get_dog_404(client):
    rv = client.get('/api/dogs/1')

    if rv.status_code != 404:
        raise AssertionError(rv.status_code)


def test_update_dog_404(client):
    rv = client.put('/api/dogs/1', json={'name': 'Scooby Doo'})

    if rv.status_code != 404:
        raise AssertionError(rv.status_code)


def test_delete_dog_404(client):
    rv = client.delete('/api/dogs/1')

    if rv.status_code != 404:
        raise AssertionError(rv.status_code)
