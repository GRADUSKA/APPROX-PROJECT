class Perso:
    # Creation d'un personnage avec le nom et ses differents traits
    def __init__(self, name, traits):
        self.name = name
        self.traits = traits

    # Voir si nous pouvons ajouter notre personnage (si le trait n'existe pas deja dans la liste)
    def compatible(self, list_traits):
        for trait in self.traits:
            if trait in list_traits:
                return False
        return True


# Creer la liste de personnage a l'aide d'un fichier input
def create_list(path):
    # All sera la list qui contiendra tous les personnages
    all = []
    f = open(path, "r")
    lines = f.readlines()
    for line in lines:
        l = line.split()
        # Si notre personnage a plus de 3 traits, nous ne voulons pas le mettre dans la liste (inutile)
        if len(l) <= 3:
            # Creation de notre liste de trait
            t = []
            t.append(l[1])
            t.append(l[2])
            # Ajout dans notre liste de personnage
            all.append(Perso(l[0],t))
    f.close()
    return all

# Permet d'avoir un joli print :)
def print_perso(all):
    # Print de tous les personnages
    for perso in all:
        print(f"Perso: {perso.name}, traits: {perso.traits}")
    # Print du nombre de personnages
    print(f"Nombre de personnage: {len(all)}")