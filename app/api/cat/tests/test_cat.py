def test_get_all_cats(client):
    rv = client.get('/api/cats/')

    if b'[]' not in rv.data:
        raise AssertionError(rv.data)
    if rv.status_code != 200:
        raise AssertionError(rv.status_code)


def test_create_cat(client):
    rv = client.post('/api/cats/', json={'id': 1, 'name': 'Felix'})

    if b'Felix' not in rv.data:
        raise AssertionError(rv.data)
    if rv.status_code != 201:
        raise AssertionError(rv.status_code)


def test_get_cat(client):
    rv = client.get('/api/cats/1')

    if b'Felix' not in rv.data:
        raise AssertionError(rv.data)
    if rv.status_code != 200:
        raise AssertionError(rv.status_code)


def test_update_cat(client):
    rv = client.put('/api/cats/1', json={'name': 'Sylvester'})

    if rv.status_code != 204:
        raise AssertionError(rv.status_code)


def test_delete_cat(client):
    rv = client.delete('/api/cats/1')

    if rv.status_code != 204:
        raise AssertionError(rv.status_code)


def test_get_cat_404(client):
    rv = client.get('/api/cats/1')

    if rv.status_code != 404:
        raise AssertionError(rv.status_code)


def test_update_cat_404(client):
    rv = client.put('/api/cats/1', json={'name': 'Sylvester'})

    if rv.status_code != 404:
        raise AssertionError(rv.status_code)


def test_delete_cat_404(client):
    rv = client.delete('/api/cats/1')

    if rv.status_code != 404:
        raise AssertionError(rv.status_code)
