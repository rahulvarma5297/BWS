import requests

while True:
    pokemon = input("Enter the Name of Pokemon : ")
    pokemon = pokemon.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        print(f"Name of the pokemon : {data['name']}")

        count = 1
        print("Abilities of the pokemon :")
        for ability in data['abilities']:
            print(count, "->", ability['ability']['name'])
            count += 1
        
        print("\n")
    else:
        print("Pokemon Not Found")