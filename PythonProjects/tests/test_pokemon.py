import requests
import pytest

URL = "https://api.pokemonbattle.me/v2/"
HEADER = {
    "Content-Type": "application/json",
    }

def test_get_trainers_status():
    """
    KTI-1. Get trainers
    """
    response = requests.get(url=f'{URL}trainers', timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_id():
    """
    KTI-1. Get trainers id
    """
    response = requests.get(url=f'{URL}trainers', params={'trainer_id': 161}, timeout=5)
    assert response.json()['trainer_name'] == 'Vlados', ''