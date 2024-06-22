import random

num_origins = int(input("Entrez le nombre d'origines à générer: "))
num_classes = int(input("Entrez le nombre de classes à générer: "))

origins = [f"Trait{i}" for i in range(num_origins)]
classes = [f"Class{i}" for i in range(num_classes)]

num_champions = int(input("Entrez le nombre de champions à générer: "))
champions = []
traits_per_champion = []

for i in range(num_champions):
    champ_name = f"Champ{i+1}"
    
    num_traits = random.randint(2, 3)
    
    traits = set()
    while len(traits) < num_traits:
        if len(traits) < 2:  # Pour avoir des classes et des origines
            trait_type = random.choice(["origin", "class"])
        else:
            trait_type = "any"
        
        if trait_type == "origin" or (trait_type == "any" and random.choice([True, False])):
            traits.add(random.choice(origins))
        else:
            traits.add(random.choice(classes))
    
    champions.append(champ_name)
    traits_per_champion.append(list(traits))

formatted_data = "\n".join([f"{champ} {' '.join(traits)}" for champ, traits in zip(champions, traits_per_champion)])

print(formatted_data)

