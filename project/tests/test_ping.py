from app import main


def test_ping(test_app):
    # given a test_app

    # when /ping
    response = test_app.get('/ping')

    # then
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}
