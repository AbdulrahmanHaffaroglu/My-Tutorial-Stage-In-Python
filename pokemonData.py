import requests

base_url = "https://pokeapi.co/api/v2/"

def getPokemonData():
    name_of_pokemon = input("Type the name of the pokemon: ")
    url =  f"{base_url}pokemon/{name_of_pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        while response.status_code != 200:
            name_of_pokemon = input("Try Again: ")
            url =  f"{base_url}pokemon/{name_of_pokemon}"
            response = requests.get(url)
    
    return response.json()

data = getPokemonData()

moves = [move["move"]["name"] for move in data["moves"]]
type = [type["type"]["name"] for type in data["types"]]

print(f"Name: {data["name"]}\n")
print(f"Height: {data["height"]}\n")
print(f"weight: {data["weight"]}\n")
print(f"types:\n {"\n".join(type)}\n")
print(f"moves:\n {"\n".join(moves)}")