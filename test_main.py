from fastapi.testclient import TestClient
from main import app
 
client = TestClient(app)
 
def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}
   
def test_check_alphabet_true():
    response = client.post("/check-alphabet/", json={"input_string": "The quick brown fox jumps over the lazy dog 123!!!"})
    assert response.status_code == 200
    assert response.json() == {"contains_all_letters": True}
   
def test_check_alphabet_false():
    response = client.post("/check-alphabet/", json={"input_string": "Hello, World!"})
    assert response.status_code == 200
    assert response.json() == {"contains_all_letters": False}
