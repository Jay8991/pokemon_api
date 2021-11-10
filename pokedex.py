

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
    
    def get_ability(self, pokemon_data):
        # get abilities cause some pokemon can have more than one ability
        abilities = []
        for j in range(len(pokemon_data.json()['abilities'])):
            abilities.append(
                {
                    'name' : pokemon_data.json()['abilities'][j]['ability']['name']
                }
            )
        return abilities
    
    def existing_class_type(self, pokemon_data, class_types):
        abilities = self.get_ability(pokemon_data)
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
            'abilities' : abilities
        })

    def new_class_type(self, pokemon_data, class_types):
        abilities = self.get_ability(pokemon_data)
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
                            'abilities' : abilities
                        }
                    ],
                }
        })

    def sort_list(self, pokemon_data):

        # loop over cause some pokemon can have more than one class type
        for i in range(len(pokemon_data.json()['types'])):
            class_types = pokemon_data.json()['types'][i]['type']['name']
            if(class_types in self.pokemon_sort):
                self.existing_class_type(pokemon_data, class_types)
            else:
                self.new_class_type(pokemon_data, class_types)

    
    def print_sort(self):
        print(self.pokemon_sort)

