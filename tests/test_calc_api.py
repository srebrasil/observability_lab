# Path: tests/test_calc_api.py
import requests
import pytest
 
def test_sum():
    num1 = 2
    num2 = 3
    expected = 5
    url = f'http://localhost:4000/api/v1/calc/sum/{num1}/{num2}'
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['result'] == expected
 
def test_sub():
    num1 = 2
    num2 = 3
    expected = -1
    url = f'http://localhost:4000/api/v1/calc/sub/{num1}/{num2}'
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['result'] == expected

def test_mult():
    num1 = 2
    num2 = 3
    expected = 6
    url = f'http://localhost:4000/api/v1/calc/mult/{num1}/{num2}'
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['result'] == expected

def test_div():
    num1 = 2
    num2 = 3
    expected = 0.6666666666666666
    url = f'http://localhost:4000/api/v1/calc/div/{num1}/{num2}'
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['result'] == expected

if __name__ == '__main__':
    pytest.main([__file__])
    url = f'http://localhost:4000/api/v1/calc/sum/{num1}/{num2}'