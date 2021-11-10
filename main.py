import requests

def directions():
    print("""Type 'show' to view Pokedex.
Type 'quit' to exit Pokedex.
Type 'sort' to view a categorized version of your Pokedex.
    """)

class Pokedex:
    def __init__(self):
         # a way to store pokemon names
        self.pokemon_names = []
        self.pokemon_sort = {}
        self.names = []
    
    def show(self):
        for i in range(len(self.pokemon_names)):
            print(f"{i+1}: {self.pokemon_names[i]}")

    def add(self, pokemon):
        self.pokemon_names.append(pokemon)

    def sort_list(self):
        for i in range(len(self.pokemon_names)):
            data = requests.get('https://pokeapi.co/api/v2/pokemon/' + self.pokemon_names[i])
            pokedex_key = data.json()['types'][0]['type']['name']
            if(pokedex_key in self.pokemon_sort):
                self.pokemon_sort[pokedex_key].append(data.json()['forms'][0]['name'])
            else:
                self.pokemon_sort.update({pokedex_key : [data.json()['forms'][0]['name']]})
        print(self.pokemon_sort)



def main():

    pokedex = Pokedex()
    directions()
    done = False
    while not done:
        populate_pokemon = input("Type in the name of the Pokemon to populate your Pokedex or type one of the commands from above. ").lower()
        # print(populate_pokemon)
        if populate_pokemon == 'show':
            pokedex.show()
        elif populate_pokemon == 'quit':
            break
        elif populate_pokemon == 'sort':
            pokedex.sort_list()
        else:
            data = requests.get('https://pokeapi.co/api/v2/pokemon/' + populate_pokemon)
            if data.status_code == 200:
                # print("In the list")
                pokedex.add(populate_pokemon)
            else:
                print("Not valid command or pokemon not valid!!")
    
    print("Thank you! Come Again.")

main()