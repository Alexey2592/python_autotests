import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '2e06f1b34918d48064b67590626c916f'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_edit = {
    "pokemon_id": "116262",
    "name": "pikachu",
    "photo_id": 2
}

body_add =  {
    "pokemon_id": "116262"
}

'''respons_create = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_create)
print(respons_create.text)'''   #создание покемона


'''respons_edit = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_edit)
print(respons_edit.text)'''   #смена имени покемона

respons_add = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_add)
print(respons_add.text)     #добавить покемона в покебол

