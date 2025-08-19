import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'введите свой токен'
HEADER = {'Content-Type':'application/json', 'trainer_token' :TOKEN}
TRAINER_ID = 'введите свой ID тренера'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' :TRAINER_ID})
    assert response.status_code == 200
    

def test_pokemon_name():
    response_get_pok_name = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' :TRAINER_ID})
    assert response_get_pok_name.json()["data"][0]["name"] == 'введите имя покемона'

def test_trainer_name():
    response_get_name = requests.get(url = f'{URL}/me', headers=HEADER)
    assert response_get_name.json()["data"][0]["trainer_name"] == "введите имя тренера"

