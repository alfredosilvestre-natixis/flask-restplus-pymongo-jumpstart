def test_get_api(client):
    rv = client.get('/api/')
    assert b'Generic API' in rv.data
