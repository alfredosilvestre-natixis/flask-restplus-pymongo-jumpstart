def test_get_all_cats(client):
    rv = client.get('/api/cats/')
    assert b'[]' in rv.data or b'"name":' in rv.data
    assert rv.status_code == 200


def test_create_cat(client):
    rv = client.post('/api/cats/', json={'id': 1, 'name': 'Felix'})
    assert b'Felix' in rv.data
    assert rv.status_code == 201


def test_get_cat(client):
    rv = client.get('/api/cats/1')
    assert b'Felix' in rv.data
    assert rv.status_code == 200


def test_update_cat(client):
    rv = client.put('/api/cats/1', json={'name': 'Sylvester'},)
    assert rv.status_code == 204


def test_delete_cat(client):
    rv = client.delete('/api/cats/1')
    assert rv.status_code == 204


def test_get_cat_404(client):
    rv = client.get('/api/cats/1')
    assert rv.status_code == 404


def test_update_cat_404(client):
    rv = client.put('/api/cats/1', json={'name': 'Sylvester'},)
    assert rv.status_code == 404


def test_delete_cat_404(client):
    rv = client.delete('/api/cats/1')
    assert rv.status_code == 404
