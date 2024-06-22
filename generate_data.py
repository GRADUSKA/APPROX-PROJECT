import random

# Listes de traits possibles
origins = ["Fated", "Ghostly", "Mythic", "Umbral", "Storyweaver", "Inkshadow", "Heavenly", "Fortune", "Dryad", "Porcelain", "Dragonlord", "Lovers"]
classes = ["Arcanist", "Sniper", "Behemoth", "Duelist", "Warden", "Reaper", "Bruiser", "Invoker", "Trickshot", "Sage", "Altruist", "Artist", "SpiritWalker"]

# Listes de noms possibles (pour simplification, nous avons des noms comme Champ1, Champ2, etc.)
num_champions = int(input())
champions = []
traits_per_champion = []

for i in range(num_champions):
    champ_name = f"Champ{i+1}"
    
    # Générer entre 2 et 3 traits pour chaque champion
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

# Formater les résultats selon la grammaire spécifiée soit nom_champion trait1 traits2 ... 
formatted_data = "\n".join([f"{champ} {' '.join(traits)}" for champ, traits in zip(champions, traits_per_champion)])

print(formatted_data)
