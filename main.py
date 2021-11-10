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
    
    def show(self):
        for i in range(len(self.pokemon_names)):
            print(f"{i+1}: {self.pokemon_names[i]}")

    def add(self, pokemon):
        self.pokemon_names.append(pokemon)

    def sort_list(self, pokemon_data):
        class_types = pokemon_data.json()['types'][0]['type']['name']
        if(class_types in self.pokemon_sort):
            self.pokemon_sort[class_types]['characters'].append(
                {
                    'name' : pokemon_data.json()['forms'][0]['name'],
                    'height' : pokemon_data.json()['height'],
                    'weight' : pokemon_data.json()['weight'],
                    'stats' : 
                        {
                            'health (hp)' : pokemon_data.json()['stats'][0]['base_stat'],
                            'attack' : pokemon_data.json()['stats'][1]['base_stat'],
                            'defense' : pokemon_data.json()['stats'][2]['base_stat'],
                            'speed' : pokemon_data.json()['stats'][5]['base_stat']
                        },
                    'abilities' : [
                            {
                                'name' : pokemon_data.json()['abilities'][0]['ability']['name']
                            },
                            {
                                'name' : pokemon_data.json()['abilities'][1]['ability']['name']
                            }
                        ]
                })
        else:
            self.pokemon_sort.update(
                {
                    class_types : 
                        {
                            'characters': [
                                {
                                    'name' : pokemon_data.json()['forms'][0]['name'],
                                    'height' : pokemon_data.json()['height'],
                                    'weight' : pokemon_data.json()['weight'],
                                    'stats' : {
                                        'health (hp)' : pokemon_data.json()['stats'][0]['base_stat'],
                                        'attack' : pokemon_data.json()['stats'][1]['base_stat'],
                                        'defense' : pokemon_data.json()['stats'][2]['base_stat'],
                                        'speed' : pokemon_data.json()['stats'][5]['base_stat']
                                    },
                                    'abilities' : [
                                        {
                                            'name' : pokemon_data.json()['abilities'][0]['ability']['name']
                                        },
                                        {
                                            'name' : pokemon_data.json()['abilities'][1]['ability']['name']
                                        }
                                    ]
                                }
                            ],
                        }
                })
    
    def print_sort(self):
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
            pokedex.print_sort()
        else:
            data = requests.get('https://pokeapi.co/api/v2/pokemon/'+ populate_pokemon)
            if data.status_code == 200:
                # print("In the list")
                pokedex.add(populate_pokemon)
                pokedex.sort_list(data)
            else:
                print("Not valid command or pokemon not valid!!")
    
    print("Thank you! Come Again.")

main()