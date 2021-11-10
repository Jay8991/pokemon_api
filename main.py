import requests
import pokedex as p

def directions():
    print("""Type 'show' to view Pokedex.
Type 'quit' to exit Pokedex.
Type 'sort' to view a categorized version of your Pokedex.
    """)

def main():

    pokedex = p.Pokedex()
    directions()
    done = False
    while not done:
        # ask user for pokemon name to populate or any commands from instructions 
        populate_pokemon = input("Type in the name of the Pokemon to populate your Pokedex or type one of the commands from above. ").lower()
        if populate_pokemon == 'show':
            pokedex.show()
        elif populate_pokemon == 'quit':
            done = True
        elif populate_pokemon == 'sort':
            pokedex.print_sort()
        else:
            # get the data of that pokemon that user entered 
            data = requests.get('https://pokeapi.co/api/v2/pokemon/'+ populate_pokemon)
            # if status is 200 that means that it exists 
            if data.status_code == 200:
                # add the pokemon 
                if(populate_pokemon in pokedex.pokemon_names):
                    print("Already in the list.")
                else:
                    pokedex.add(populate_pokemon)
                    # sort it as you add it 
                    pokedex.sort_list(data)
                    # pokedex.get_statistics()
            else:
                print("Not valid command or pokemon not valid!!")
    
    print("Thank you! Come Again.")

main()