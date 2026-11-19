import json

with open("./pokedex.json", encoding="utf8") as file:
	data = json.load(file)
with open("./moves.json", encoding="utf8") as file:
	moves = json.load(file)


def name_of(pokemon, language="english"):
	name = pokemon["name"]
	return name.get(language, name.get("english", "Unknown")) if isinstance(name, dict) else name


def list_pokemon(language):
	print("Progress: ", end="", flush=True)
	for pokemon in data:
		print(name_of(pokemon, language))
		print(".", end="", flush=True)
	print(" complete")


