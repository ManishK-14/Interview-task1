from itertools import combinations

pokemons = {
    'Pikachu': ('Electric',),
    'Charizard': ('Fire','Flying'),
    'Lapras': ('Water','Ice'),
    'Machamp': ('Fighting',),
    'Mewtwo': ('Psychic','Fighting'),
    'Hoopa': ('Psychic','Ghost','Dark'),
    'Squirtle': ('Water',),
    'Gengar': ('Ghost','Poison'),
    'Onix': ('Rock','Ground')    
}

team_size = 3   # instead of "k"
all_possible_teams = combinations(pokemons.keys(), team_size)

best_team = None
max_type_count = 0

for team in all_possible_teams:
    types = set()
    for name in team:
        types.update(pokemons[name])
    
    if len(types) > max_type_count:
        max_type_count = len(types)
        best_team = (team, types)

print("Best Team:", ", ".join(best_team[0]))
print("Covers Types:", ", ".join(best_team[1]))
print("Number of Types:", max_type_count)
