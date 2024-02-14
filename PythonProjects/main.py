"""
Pokemons api
"""
import requests

URL = "https://api.pokemonbattle.me/v2/"
HEADER = {
    "Content-Type": "application/json",
    "trainer_token": "f1687bf344ad3e7704965efaafdcd520"
    }

body = {
    "name": "Raiden",
    "photo": "https://dolnikov.ru/pokemons/albums/034.png"
}

response =requests.post(url=f'{URL}pokemons', json=body, headers=HEADER, timeout=5)
print(f'Код ответа: {response.status_code}. Сообщение:{response.text}')

body = {
    "pokemon_id": "532",
    "name": "Baal",
    "photo": "https://dolnikov.ru/pokemons/albums/018.png"
}

response =requests.put(url=f'{URL}pokemons', json=body, headers=HEADER, timeout=5)
print(f'Код ответа: {response.status_code}. Сообщение:{response.text}')

body = {
    "pokemon_id": "532"
}

response =requests.post(url=f'{URL}trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(f'Код ответа: {response.status_code}. Сообщение:{response.text}')