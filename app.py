import json

with open("./pokedex.json", encoding="utf8") as file:
	data = json.load(file)
with open("./moves.json", encoding="utf8") as file:
	moves = json.load(file)


def name_of(pokemon, language="english"):
	name = pokemon["name"]
	return name.get(language, name.get("english", "Unknown")) if isinstance(name, dict) else name


def list_pokemon(language):
	for pokemon in data:
		print(name_of(pokemon, language))


def find_type(kind):
	return search(lambda p: kind.lower() in [t.lower() for t in p.get("type", [])])


def find_name(query):
	return search(lambda p: query.lower() in name_of(p).lower())


def search(matches):
	found = [p for p in data if matches(p)]
	print(*(name_of(p) for p in found), sep="\n") if found else print("No Pokemon found.")
	return found


def show_moves(query):
	pokemon = next((p for p in data if query.lower() in name_of(p).lower()), None)
	if not pokemon:
		print("No Pokemon found.")
		return
	types = {t.lower() for t in pokemon.get("type", [])}
	records = moves.values() if isinstance(moves, dict) else moves
	found = [m for m in records if str(m.get("type", "")).lower() in types]
	print(*(m.get("name", m.get("ename", "Unknown")) for m in found), sep="\n")


choice = input("1: list by language, 2: search type, 3: search name, 4: moves: ")
if choice == "1":
	list_pokemon(input("Language (english/japanese/chinese/french): ").lower())
elif choice == "2":
	find_type(input("Pokemon type: "))
elif choice == "3":
	find_name(input("Pokemon name: "))
elif choice == "4":
	show_moves(input("Pokemon name: "))


