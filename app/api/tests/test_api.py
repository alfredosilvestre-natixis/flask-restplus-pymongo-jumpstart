def test_get_api(client):
    rv = client.get('/api/')

    if b'Generic API' not in rv.data:
        raise AssertionError(rv.data)
