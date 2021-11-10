# to get the average
import statistics as s 
import pprint as pp

class Pokedex:
    def __init__(self):
         # a way to store pokemon names and dict for sort
        self.pokemon_names = []
        self.pokemon_sort = {}
    
    def show(self):
        for i in range(len(self.pokemon_names)):
            print(f"{i+1}: {self.pokemon_names[i]}")

    def add(self, pokemon):
        self.pokemon_names.append(pokemon)
    
    # get abilities cause some pokemon can have more than one ability
    def get_ability(self, pokemon_data):
        pokemon_abilities = []
        for j in range(len(pokemon_data.json()['abilities'])):
            pokemon_abilities.append(
                {
                    'name' : pokemon_data.json()['abilities'][j]['ability']['name']
                }
            )
        return pokemon_abilities
    
    def get_statistics(self):
        avg_height = []
        for key in self.pokemon_sort:
            for i in range(len(self.pokemon_sort[key]['characters'])):
                avg_height.append(self.pokemon_sort[key]['characters'][i]['height'])
        return avg_height
    
    def existing_class_type(self, pokemon_data, class_types):
        # the class name exists so just need to append the data to that class name 
        # get it's abilities so can later append it 
        pokemon_abilities = self.get_ability(pokemon_data)
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
            'abilities' : pokemon_abilities
        })

    def new_class_type(self, pokemon_data, class_types):
        pokemon_abilities = self.get_ability(pokemon_data)
        height = self.get_statistics()
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
                            'abilities' : pokemon_abilities
                        }
                    ]
                    # 'statistics' : {
                    #     "average height" : height,
                    #     "average weight" : 0,
                    #     "average health" : 0,
                    #     "average attack" : 0,
                    #     "average defense" : 0,
                    #     "average speed" : 0
                    # }
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
        pp.pprint(self.pokemon_sort)

