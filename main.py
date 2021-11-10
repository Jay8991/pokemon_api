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