import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'введите свой токен'
HEADER ={'Content-Type':'application/json', 'trainer_token' :TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "введите почту",  // введите свою почту
    "password": "введите пароль" //введите свой пароль
}
body_create = {
    "name": "Puipui", # придумайте имя для покемона или можно сгенерировать случайные значения для имени передав строку "generate"
    "photo_id": "850"  # аватар для покемона от 1 до 1000 или можно сгенерировать случайное фото передав число -1
}
body_rename = {"pokemon_id": "288391",
    "name": "Chuichui",
    "photo_id": 850
    }
body_add_pokeball = {"pokemon_id": "279992"}

'''response = requests.post(url = f'{URL}/trainers/reg', headers=HEADER, json=body_registration)
print(response.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_rename)
print(response_rename.text)'''

response_add_pokeball = requests.post(url =f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(response_add_pokeball.text)

